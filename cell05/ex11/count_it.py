#!/usr/bin/python3

import sys

if len(sys.argv) < 2:
    print("none\n")
else:
    param_length = len(sys.argv) - 1
    print(f'parameters: {param_length}')

    for i in range(0, len(sys.argv)):
        word = sys.argv[i]
        count = len(sys.argv[i])
        print(f"{word}: {count}")
