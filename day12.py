# Day 12: Subterranean Sustainability

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

initial_state = data[0].split(':')[1].strip()
rules = {}
for rule in data[2:]:
    k, v = rule.split(' => ')
    rules[k] = v

pots = []
for i, char in enumerate(initial_state):
    pots.append([i, char])
# print(pots)

current_state = initial_state
generations = 20
margin = 4
for g in range(generations):
    # current_state = spread(current_state)
    # add a few empty pots on either side
    min_idx = pots[0][0]
    for j in range(margin):
        pots.insert(0, [min_idx - (j + 1), '.'])
        max_idx = pots[-1][0]
        pots.append([max_idx + 1, '.'])
    # look for matches
    next_gen = []
    for i in range(len(pots)):
        if 1 < i < len(pots) - 2:
            current_slice = ''
            for k in range(5):
                current_slice += pots[i-2+k][1]
            if current_slice in rules:
                next_gen.append([pots[i][0], rules[current_slice]])
            else:
                next_gen.append([pots[i][0], '.'])
        else:
            next_gen.append(pots[i])
    pots = next_gen
    # print(f"After generation {g+1}: ")
    # print(f"      min index = {pots[0][0]}, max index = {pots[-1][0]}")
    # print(''.join([pot[1] for pot in pots]))


# print(pots)

ans = 0
for idx, pot in pots:
    if pot == '#':
        ans += idx
print(ans)
