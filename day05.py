# Day 5: Alchemical Reduction

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")


def reacted_length(polymer):
    stack = []

    for unit in polymer:
        if stack and stack[-1] != unit and stack[-1].lower() == unit.lower():
            stack.pop()
        else:
            stack.append(unit)
    return len(stack)


print(reacted_length(data[0]))

# Part 2
shortest_polymer_length = len(data[0])
for i in range(26):
    suspect_unit = chr(ord('A') + i)
    new_polymer = ''.join(
        c for c in data[0] if c not in [suspect_unit, suspect_unit.lower()]
    )
    polymer_length = reacted_length(new_polymer)
    if polymer_length < shortest_polymer_length:
        shortest_polymer_length = polymer_length

print(shortest_polymer_length)
