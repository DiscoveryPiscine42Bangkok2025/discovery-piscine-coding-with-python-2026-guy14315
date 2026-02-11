#!/usr/bin/python3

arr = [2, 8, 9, 48, 8, 22, -12, 2]
new_set = set()

for i in arr:
    if i > 5:
        new_set.add(i + 2)

print(arr)
print(new_set)
