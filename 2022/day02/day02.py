from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

lines = file.readlines()
score = 0

for line in lines:
    line = line.replace("\n", "")
    parts = line.split(" ")
    
    match parts[1]:
        case "X":
            score += 1
        case "Y":
            score += 2
        case "Z":
            score += 3
    
    if ((parts[0] == "A" and parts[1] == "X") or
        (parts[0] == "B" and parts[1] == "Y") or
        (parts[0] == "C" and parts[1] == "Z")):
        score += 3
        
    if ((parts[0] == "A" and parts[1] == "Y") or
        (parts[0] == "B" and parts[1] == "Z") or
        (parts[0] == "C" and parts[1] == "X")):
        score += 6

print("Part One: {}".format(score))
        
from rps import RPS

score = 0
for line in lines:
    line = line.replace("\n", "")
    parts = line.split(" ")
    rps = RPS(parts[0])
    choice = ""
    
    match parts[1]:
        case "X":
            choice = rps.get_lose_choice()
        case "Y":
            choice = rps.get_draw_choice()
        case "Z":
            choice = rps.get_win_choice()
            
    
    match choice:
        case "A":
            score += 1
        case "B":
            score += 2
        case "C":
            score += 3
    
    if (parts[1] == "Y"):
        score += 3
        
    if (parts[1] == "Z"):
        score += 6
        
print("Part Two: {}".format(score))