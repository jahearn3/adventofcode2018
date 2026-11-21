# Day 13: Mine Cart Madness

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = [list(row) for row in ld.load_data(f"example{day}.txt")]
data = [list(row) for row in ld.load_data(f"input{day}.txt")]

carts = []

for i, row in enumerate(data):
    for j, char in enumerate(row):
        if char in ['v', '^', '<', '>']:
            carts.append({
                'position': [j, i],
                'orientation': char,
                'n_turns': 0})
            if char in ['v', '^']:
                data[i][j] = '|'
            elif char in ['<', '>']:
                data[i][j] = '-'

t = 0
collision = False
while not collision:
    carts.sort(key=lambda cart: (cart['position'][1], cart['position'][0]))
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
        if cart['orientation'] == '>' and next_track == '-':
            cart['position'] = [x+1, y]
        elif cart['orientation'] == '<' and next_track == '-':
            cart['position'] = [x-1, y]
        elif cart['orientation'] == '^' and next_track == '|':
            cart['position'] = [x, y-1]
        elif cart['orientation'] == 'v' and next_track == '|':
            cart['position'] = [x, y+1]
        # 2. Turns without options
        elif cart['orientation'] == '>' and next_track == '/':
            cart['position'] = [x+1, y]
            cart['orientation'] = '^'
        elif cart['orientation'] == '>' and next_track == '\\':
            cart['position'] = [x+1, y]
            cart['orientation'] = 'v'
        elif cart['orientation'] == '<' and next_track == '/':
            cart['position'] = [x-1, y]
            cart['orientation'] = 'v'
        elif cart['orientation'] == '<' and next_track == '\\':
            cart['position'] = [x-1, y]
            cart['orientation'] = '^'
        elif cart['orientation'] == '^' and next_track == '/':
            cart['position'] = [x, y-1]
            cart['orientation'] = '>'
        elif cart['orientation'] == '^' and next_track == '\\':
            cart['position'] = [x, y-1]
            cart['orientation'] = '<'
        elif cart['orientation'] == 'v' and next_track == '/':
            cart['position'] = [x, y+1]
            cart['orientation'] = '<'
        elif cart['orientation'] == 'v' and next_track == '\\':
            cart['position'] = [x, y+1]
            cart['orientation'] = '>'
        # 3. Turns with options
        elif cart['orientation'] == '>' and next_track == '+':
            cart['position'] = [x+1, y]
            if cart['n_turns'] % 3 == 0:
                cart['orientation'] = '^'
            elif cart['n_turns'] % 3 == 2:
                cart['orientation'] = 'v'
            cart['n_turns'] += 1
        elif cart['orientation'] == '<' and next_track == '+':
            cart['position'] = [x-1, y]
            if cart['n_turns'] % 3 == 0:
                cart['orientation'] = 'v'
            elif cart['n_turns'] % 3 == 2:
                cart['orientation'] = '^'
            cart['n_turns'] += 1
        elif cart['orientation'] == '^' and next_track == '+':
            cart['position'] = [x, y-1]
            if cart['n_turns'] % 3 == 0:
                cart['orientation'] = '<'
            elif cart['n_turns'] % 3 == 2:
                cart['orientation'] = '>'
            cart['n_turns'] += 1
        elif cart['orientation'] == 'v' and next_track == '+':
            cart['position'] = [x, y+1]
            if cart['n_turns'] % 3 == 0:
                cart['orientation'] = '>'
            elif cart['n_turns'] % 3 == 2:
                cart['orientation'] = '<'
            cart['n_turns'] += 1
        else:
            print('Unknown error:')
            print('cart', cart)
            print('next track', next_track)
            collision = True
            break
        for other in carts:
            if other is not cart and other['position'] == cart['position']:
                print('Collision detected at', cart['position'])
                collision = True
                break
        if collision:
            break
    t += 1

# Part 2
data = [list(row) for row in ld.load_data(f"example{day}.txt")]
data = [list(row) for row in ld.load_data(f"input{day}.txt")]

carts = []

for i, row in enumerate(data):
    for j, char in enumerate(row):
        if char in ['v', '^', '<', '>']:
            carts.append({
                'position': [j, i],
                'orientation': char,
                'n_turns': 0})
            if char in ['v', '^']:
                data[i][j] = '|'
            elif char in ['<', '>']:
                data[i][j] = '-'

while len(carts) > 1:
    carts.sort(key=lambda cart: (cart['position'][1], cart['position'][0]))
    new_carts = []
    for cart in carts:
        next_track = None
        x, y = cart['position']
        if cart['orientation'] == '0':
            continue
        elif cart['orientation'] == '>':
            next_track = data[y][x+1]
        elif cart['orientation'] == '<':
            next_track = data[y][x-1]
        elif cart['orientation'] == '^':
            next_track = data[y-1][x]
        elif cart['orientation'] == 'v':
            next_track = data[y+1][x]
        else:
            print('Error: Path off track')
            break

        # Update positions
        # 1. No turns
        if cart['orientation'] == '>' and next_track == '-':
            cart['position'] = [x+1, y]
        elif cart['orientation'] == '<' and next_track == '-':
            cart['position'] = [x-1, y]
        elif cart['orientation'] == '^' and next_track == '|':
            cart['position'] = [x, y-1]
        elif cart['orientation'] == 'v' and next_track == '|':
            cart['position'] = [x, y+1]
        # 2. Turns without options
        elif cart['orientation'] == '>' and next_track == '/':
            cart['position'] = [x+1, y]
            cart['orientation'] = '^'
        elif cart['orientation'] == '>' and next_track == '\\':
            cart['position'] = [x+1, y]
            cart['orientation'] = 'v'
        elif cart['orientation'] == '<' and next_track == '/':
            cart['position'] = [x-1, y]
            cart['orientation'] = 'v'
        elif cart['orientation'] == '<' and next_track == '\\':
            cart['position'] = [x-1, y]
            cart['orientation'] = '^'
        elif cart['orientation'] == '^' and next_track == '/':
            cart['position'] = [x, y-1]
            cart['orientation'] = '>'
        elif cart['orientation'] == '^' and next_track == '\\':
            cart['position'] = [x, y-1]
            cart['orientation'] = '<'
        elif cart['orientation'] == 'v' and next_track == '/':
            cart['position'] = [x, y+1]
            cart['orientation'] = '<'
        elif cart['orientation'] == 'v' and next_track == '\\':
            cart['position'] = [x, y+1]
            cart['orientation'] = '>'
        # 3. Turns with options
        elif cart['orientation'] == '>' and next_track == '+':
            cart['position'] = [x+1, y]
            if cart['n_turns'] % 3 == 0:
                cart['orientation'] = '^'
            elif cart['n_turns'] % 3 == 2:
                cart['orientation'] = 'v'
            cart['n_turns'] += 1
        elif cart['orientation'] == '<' and next_track == '+':
            cart['position'] = [x-1, y]
            if cart['n_turns'] % 3 == 0:
                cart['orientation'] = 'v'
            elif cart['n_turns'] % 3 == 2:
                cart['orientation'] = '^'
            cart['n_turns'] += 1
        elif cart['orientation'] == '^' and next_track == '+':
            cart['position'] = [x, y-1]
            if cart['n_turns'] % 3 == 0:
                cart['orientation'] = '<'
            elif cart['n_turns'] % 3 == 2:
                cart['orientation'] = '>'
            cart['n_turns'] += 1
        elif cart['orientation'] == 'v' and next_track == '+':
            cart['position'] = [x, y+1]
            if cart['n_turns'] % 3 == 0:
                cart['orientation'] = '>'
            elif cart['n_turns'] % 3 == 2:
                cart['orientation'] = '<'
            cart['n_turns'] += 1
        else:
            print('Unknown error:')
            print('cart', cart)
            print('next track', next_track)
            break
        for other in carts:
            if (other is not cart
                    and other['orientation'] != '0'
                    and other['position'] == cart['position']):
                print('Collision detected at', cart['position'])
                cart['orientation'] = '0'
                other['orientation'] = '0'
    for cart in carts:
        if cart['orientation'] != '0':
            new_carts.append(cart)
    carts = new_carts
    t += 1

print(carts)
