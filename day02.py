# Day 2: Inventory Management System

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

# data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

# Part 1
twos = 0
threes = 0

for line in data:
    two = False
    three = False
    for char in line:
        count = line.count(char)
        if count == 2:
            two = True
        if count == 3:
            three = True
    if two:
        twos += 1
    if three:
        threes += 1

print(twos * threes)

# Part 2


def find_one_diff(strings):
    seen = set()
    for s in strings:
        for i in range(len(s)):
            pattern = s[:i] + '*' + s[i+1:]
            if pattern in seen:
                return pattern
            else:
                seen.add(pattern)
    return None


match = find_one_diff(data)
for c in range(len(match)):
    if match[c] == '*':
        print(match[:c] + match[c+1:])
