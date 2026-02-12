def checkmate(board):

    ## Empty board
    if not board:
        print("Fail")
        return

    rows_str = [line.strip() for line in board.strip().splitlines()]

    # Clean the board with unknown char to '.'
    rows = []
    for line in rows_str:
        clean_row = []
        for char in line:
            if char in "KQBRP":
                clean_row.append(char)
            else:
                clean_row.append('.')
        rows.append(clean_row)

    if not rows or len(rows) != len(rows[0]):
        print("Fail")
        return

    ischeck = False

    for i in range(len(rows)):

        if len(rows[i]) != len(rows):
            print("Fail")
            return

        for j in range(len(rows[i])):
            piece = rows[i][j]

            if piece == "P":
                if checkP(i, j, rows): ischeck = True
            elif piece == "B":
                if checkB(i, j, rows): ischeck = True
            elif piece == "R":
                if checkR(i, j, rows): ischeck = True
            elif piece == "Q":
                if checkQ(i, j, rows): ischeck = True

            if ischeck:
                break

        if ischeck:
            break

    if ischeck:
        print("Success")
    else:
        print("Fail")

# Helper functions
def checkP(row, col, board):
    if (row -1 >= 0 
        and col - 1 >= 0 
        and board[row-1][col-1] == "K"):
        return True

    elif (row - 1 >= 0
        and col + 1 < len(board[row]) 
        and board[row - 1][col + 1] == "K"):
        return True
    
    return False

def checkB(row, col, board):
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    b_len = len(board)
    
    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < b_len and 0 <= c < b_len:
            if board[r][c] == "K":
                return True
            if board[r][c] != ".": #blocker
                break
            r += dr
            c += dc
    return False
    


def checkR(row, col, board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    b_len = len(board)

    for dr, dc in directions:
        r, c = row + dr, col + dc
        while 0 <= r < b_len and 0 <= c < b_len:
            if board[r][c] == "K":
                return True
            if board[r][c] != ".":  # blocker
                break

            r += dr
            c += dc
    return False


def checkQ(row, col, board):
    return checkB(row, col, board) or checkR(row, col, board)
