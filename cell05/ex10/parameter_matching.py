#!/usr/bin/python3

import sys

if len(sys.argv) != 2:
    print("none\n")

parameter = sys.argv[1]

while True:
    user_input = input("What was the parameter? ").strip()
    if user_input == parameter:
        print("Good job!")
        break
    else:
        print("Nope, sorry...")
