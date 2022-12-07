from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

from statistics import mean

lines = file.read().split("\n")
bit_range = len(lines[0])

gamma = ""
epsilon = ""
for i in range(bit_range):
    if mean(int(line[i]) for line in lines) >= 0.5:
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

print("Part One: {}".format(int(gamma, 2) * int(epsilon, 2)))

oxy = lines.copy()
co2 = lines.copy()
for i in range(bit_range):
    if len(oxy) == 1:
        break
    if mean(int(value[i]) for value in oxy) >= 0.5:
        oxy = [v for v in oxy if v[i] == "1"]
    else:
        oxy = [v for v in oxy if v[i] == "0"]
    
for i in range(bit_range):
    if len(co2) == 1:
        break
    if mean(int(value[i]) for value in co2) >= 0.5:
        co2 = [v for v in co2 if v[i] == "0"]
    else:
        co2 = [v for v in co2 if v[i] == "1"]
    
print("Part Two: {}".format(int(oxy[0], 2) * int(co2[0], 2)))