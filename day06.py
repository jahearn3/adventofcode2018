# Day 6: Chronal Coordinates

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

grid = {}
pairs = []
max_x, max_y = 0, 0
for line in data:
    coords = line.split(',')
    x = int(coords[0])
    y = int(coords[1].strip())
    if x > max_x:
        max_x = x
    if y > max_y:
        max_y = y
    pairs.append((x, y))

margin = 10
for i in range(-margin, max_x + margin):
    for j in range(-margin, max_y + margin):
        closest_distance = max_x + max_y + margin
        closest = None
        for (x, y) in pairs:
            distance = abs(x - i) + abs(y - j)
            if distance < closest_distance:
                closest_distance = distance
                closest = (x, y)
            elif distance == closest_distance:
                closest = None
        grid[(i, j)] = {'closest': closest, 'distance': closest_distance}

# Anything on the outer edge belongs to an infinite area
forbidden = []
maxx = max_x + margin - 1
maxy = max_y + margin - 1
for k, v in grid.items():
    (i, j) = k
    if v["closest"] is None:
        continue
    if i == -margin or i == maxx or j == -margin or j == maxy:
        if v["closest"] not in forbidden:
            forbidden.append(v["closest"])

areas = {}
for k, v in grid.items():
    if v["closest"] is None:
        continue
    if v["closest"] not in forbidden:
        if v["closest"] not in areas:
            areas[v["closest"]] = 0
        areas[v["closest"]] += 1

largest_area = 0
for k, v in areas.items():
    if v > largest_area:
        largest_area = v

print(largest_area)
