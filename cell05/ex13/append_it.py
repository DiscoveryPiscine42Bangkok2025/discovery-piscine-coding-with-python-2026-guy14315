#!/usr/bin/python3

import sys
if len(sys.argv) < 2:
    print("none")
else:
    args = sys.argv[1:]
    for i in args:
        if i.endswith("ism"):
            continue
        print(f"{i}ism")
