#!/usr/bin/python3

import sys

if len(sys.argv) < 3:
    print("none\n")
else:
    for i in range(len(sys.argv) - 1, 0, -1):
        print(sys.argv[i] + "\n")
