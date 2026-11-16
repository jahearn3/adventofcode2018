# Day 13: Mine Cart Madness

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
# data = ld.load_data(f"input{day}.txt")

carts = []

for i, row in enumerate(data):
    for j, char in enumerate(row):
        if char in ['v', '^', '<', '>']:
            carts.append({
                'position': [j, i],
                'orientation': char,
                'n_turns': 0})

t = 0
collision = False
while not collision:
    for cart in carts:
        next_track = None
        x, y = cart['position']
        if cart['orientation'] == '>':
            next_track = data[y][x+1]
        elif cart['orientation'] == '<':
            next_track = data[y][x-1]
        elif cart['orientation'] == '^':
            next_track = data[y-1][x]
        elif cart['orientation'] == 'v':
            next_track = data[y+1][x]
        else:
            print('Error: Path off track')
            collision = True
            break

        # Update positions
        # 1. No turns

        # 2. Turns without options

        # 3. Turns with options
