# Day 3: No Matter How You Slice It

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

# data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

# Part 1
ans = 0
grid = {}
for line in data:
    contents = line.split()
    id = int(contents[0][1:])
    location = contents[2].strip(':').split(',')
    x, y = int(location[0]), int(location[1])
    size = contents[3].split('x')
    width, height = int(size[0]), int(size[1])
    for i in range(x, x + width):
        for j in range(y, y + height):
            if (i, j) not in grid:
                grid[(i, j)] = [id]
            else:
                grid[(i, j)].append(id)

for k, v in grid.items():
    if len(v) > 1:
        ans += 1

print(ans)

# Part 2
ids = list(range(1, len(data) + 1))
for k, v in grid.items():
    if len(v) > 1:
        for vv in v:
            ids[vv - 1] = 0

print(sum(ids))
