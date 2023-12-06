from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

lines = lines = file.read().split("\n")

red_limit, green_limit, blue_limit = 12, 13, 14

id_sum = 0
power_sum = 0

for line in lines:
    max_cubes = {"red": 0, "green": 0, "blue": 0}
    line = [l.strip() for l in line.split(": ")]
    game_id = int(line[0].split(" ")[1])
    
    line = [l.strip() for l in line[1].split("; ")]
    
    for element in line:
        element = [e.strip() for e in element.split(", ")]
        
        for e in element:
            value, key = e.split(" ")
            max_cubes[key] = max(max_cubes[key], int(value))
        
    if max_cubes["red"] <= red_limit and max_cubes["green"] <= green_limit and max_cubes["blue"] <= blue_limit:
        id_sum += game_id
                
    power = 1
    for e in max_cubes.values():
        power *= e
    power_sum += power
        
print("Part One: {}".format(id_sum))
print("Part Two: {}".format(power_sum))
