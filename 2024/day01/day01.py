from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

lines = file.read().strip().split("\n")

import numpy as np

left = np.zeros(len(lines), np.int32)
right = np.zeros(len(lines), np.int32)

for i, line in enumerate(lines):
    elem = line.split("   ")
    left[i] = int(elem[0])
    right[i] = int(elem[1])

left.sort()
right.sort()

total_sum = 0
for i in range(len(left)):
    dist = left[i] - right[i]
    total_sum += abs(dist)

print("Part One: {}".format(total_sum))

new_left = np.unique(left)

unique, counts = np.unique(right, return_counts=True)
right_counts = dict(zip(unique, counts))

total_sum = 0
for elem in new_left:
    if elem in right_counts.keys():
        total_sum += elem * right_counts[elem]

print("Part Two: {}".format(total_sum))