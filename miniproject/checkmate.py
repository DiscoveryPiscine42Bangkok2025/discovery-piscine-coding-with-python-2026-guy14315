def checkmate(board):

    # Empty board
    if not board:
        print("Error empty board.")
        return

    rows_str = [line.strip() for line in board.strip().splitlines()]

    # Check invalid char and number of king
    rows = []
    king_count = 0
    for line in rows_str:
        if len(rows_str) != len(line): # Check col-row equal size
            print("Error: not square.")
            return
        clean_row = []
        for char in line:

            if char in "KQBRP.":
                clean_row.append(char)

                if char == "K":
                    king_count += 1

                    if king_count > 1:
                        print("Error: There is more than 1 king.")
                        return
            # not piece(PQBRP)
            else:
                clean_row.append('.')

        rows.append(clean_row)

    if king_count != 1:
        print("Error: There is no king.")
        return

    ischeck = False

    for i in range(len(rows)):

        for j in range(len(rows[i])):
            piece = rows[i][j]

            if piece == "P":
                ischeck = checkP(i, j, rows)
            elif piece == "B":
                ischeck = checkB(i, j, rows)
            elif piece == "R":
                ischeck = checkR(i, j, rows)
            elif piece == "Q":
                ischeck = checkQ(i, j, rows)

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
