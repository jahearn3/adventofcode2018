# Day 8: Memory Maneuver

import load_data as ld
import os

f = os.path.basename(__file__)
day = f[3:5]

data = ld.load_data(f"example{day}.txt")
data = ld.load_data(f"input{day}.txt")

numbers = list(map(int, data[0].split(' ')))


def parse_node(index):
    child_count, metadata_count = numbers[index:index + 2]
    index += 2

    metadata_sum = 0
    for _ in range(child_count):
        index, child_sum = parse_node(index)
        metadata_sum += child_sum

    metadata_sum += sum(numbers[index:index + metadata_count])
    return index + metadata_count, metadata_sum


end, answer = parse_node(0)
print(answer)
