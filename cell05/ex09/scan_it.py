#!/usr/bin/python3

import sys

if len(sys.argv) != 3:
    print("none\n")

key = sys.argv[1]
string = sys.argv[2]

count = string.count(key)

if count > 0:
    print(count)
else:
    print("none\n")
