# Day 5: Alchemical Reduction

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

# reactions = -1
# line = data[0]
# iterations = 0

# while reactions != 0:
#     reactions = 0
#     c = 1
#     while c < len(line):
#         if line[c] != line[c-1] and line[c].lower() == line[c-1].lower():
#             line = line[:c-1] + line[c+1:]
#             reactions += 1
#             c -= 1
#         else:
#             c += 1
#     iterations += 1
#     print(iterations, reactions, len(line))

# print(len(line))

# line = data[0]
# lo = []
# hi = []
# i = 1
# reactions = 0

# while i < len(line):
#     if line[i] != line[i-1] and line[i].lower() == line[i-1].lower():
#         reactions += 1

line = data[0]
eliminations = 0

for c in range(1, len(line)):
    if line[c] != line[c-1] and line[c].lower() == line[c-1].lower():
        eliminations += 1

print(len(line) - (2 * eliminations))  # Upper bound: 20,520


def eliminate(line):
    eliminations = 0
    c = 1
    while c < len(line):
        if line[c] != line[c-1] and line[c].lower() == line[c-1].lower():
            eliminations += 1
            line = line[:c-1] + line[c+1:]
            c -= 1
        else:
            c += 1
    return line, eliminations


old_line = line
new_eliminations = -1
# print(old_line)
while new_eliminations != 0:
    new_line, new_eliminations = eliminate(old_line)
    print(len(new_line), new_eliminations)
    old_line = new_line

print(len(new_line))
