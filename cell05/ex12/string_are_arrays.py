#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    output = ""
    for char in sys.argv[1]:
        if char == 'z':
            output += char

if output == "":
    print("none")
else:
    print(output)
