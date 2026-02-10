#!/usr/bin/python3

user_input = input("What you gotta say? : ").strip()

while True:
    user_input = input("I got that! Anything else? : ").strip()
    if user_input == "STOP":
        break
