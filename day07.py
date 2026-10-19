# Day 7: The Sum of Its Parts

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
# data = ld.load_data(f"input{day}.txt")

steps_forward = {}
steps_backward = {}

# graph?

for line in data:
    words = line.split()
    prerequisite = words[1]
    step = words[7]
    if step not in steps_backward:
        steps_backward[step] = []
    steps_backward[step].append(prerequisite)
    if prerequisite not in steps_forward:
        steps_forward[prerequisite] = []
    steps_forward[prerequisite].append(step)

print(steps_forward)
print(steps_backward)

stack = []
for k, v in steps_forward.items():
    if k not in steps_backward.keys():
        stack.append(k)

print(stack)
ans = ''
while stack:
    current = sorted(stack)
    stack = []
    for item in current:
        if item in steps_forward:
            vv = steps_forward[item]
            for v in vv:
                stack.append(v)
        ans += item
print(ans)
