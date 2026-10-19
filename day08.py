# Day 8: Memory Maneuver

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
# data = ld.load_data(f"input{day}.txt")

lst = list(map(int, data[0].split(' ')))
print(lst)
n_child_nodes = lst[0]
n_metadata_entries = lst[1]
root = {
    'header': [n_child_nodes, n_metadata_entries],
    'child_nodes': [],
    'metadata_entries': []
    }

ans = 0
for i in range(2, len(lst)):
    n = int(lst[i])

print(ans)
