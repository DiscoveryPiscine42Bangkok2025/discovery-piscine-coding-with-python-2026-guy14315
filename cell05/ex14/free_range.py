#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    arr = []
    start = int(sys.argv[1]) 
    stop = int(sys.argv[2]) + 1
    for i in range(start, stop):
        arr.append(i)
print(arr)
