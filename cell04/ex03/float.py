#!/usr/bin/python3

number = input("Give me a number: ")
converted_number = float(number)

if converted_number.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")
