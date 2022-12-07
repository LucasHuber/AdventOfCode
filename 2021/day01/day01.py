from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

lines = file.read().split("\n")
count = 0

prev = int(lines[0])
for line in lines[1:]:
    if int(line) > prev:
        count += 1
    prev = int(line)
    
print("Part One: {}".format(count))

count = 0
prev = int(lines[0]) + int(lines[1]) + int(lines[2])
i = 1
while i < len(lines) - 2:
    current = int(lines[i]) + int(lines[i+1]) + int(lines[i+2])
    if current > prev:
        count += 1
    prev = current
    i += 1
    
print("Part Two: {}".format(count))