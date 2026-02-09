#!/usr/bin/python3

number1 = int(input("Enter first number:\n"))
number2 = int(input("Enter second number:\n"))
result = number1 * number2

print(f'{number1} x {number2}\n')

if result == 0:
    print("This result is positive and negative.")
elif result < 0:
    print("This result is negative.")
else:
    print("This result is positive.")
