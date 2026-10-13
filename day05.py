# Day 5: Alchemical Reduction

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

reactions = -1
line = data[0]
iterations = 0

while reactions != 0:
    reactions = 0
    c = 1
    while c < len(line):
        if line[c] != line[c-1] and line[c].lower() == line[c-1].lower():
            line = line[:c-1] + line[c+1:]
            reactions += 1
            c -= 1
        else:
            c += 1
    iterations += 1
    # print(iterations, reactions, len(line))

print(len(line))
