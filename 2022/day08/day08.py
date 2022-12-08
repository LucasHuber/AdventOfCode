from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

lines = file.read().split("\n")
x_max, y_max = len(lines[0]) - 1, len(lines) - 1	# index maxima
visible = 2 * len(lines[0]) + 2 * len(lines) - 4	# outer trees

def check_single_direction_visible(x: int, y: int, from_max: bool, x_direction: bool) -> bool:
    height = int(lines[y][x])
    if x_direction:
        initial = x
        x = x_max if from_max else 0
        while x > initial if from_max else x < initial:
            if int(lines[y][x]) >= height:
                break
            x += -1 if from_max else 1
            if x == initial:
                return True
        return False
    else:
        initial = y
        y = y_max if from_max else 0
        while y > initial if from_max else y < initial:
            if int(lines[y][x]) >= height:
                break
            y += -1 if from_max else 1
            if y == initial:
                return True
        return False

def check_if_visible(x: int, y: int) -> bool:
    left = check_single_direction_visible(x, y, from_max=False, x_direction=True)
    right = check_single_direction_visible(x, y, from_max=True, x_direction=True)
    up = check_single_direction_visible(x, y, from_max=False, x_direction=False)
    down = check_single_direction_visible(x, y, from_max=True, x_direction=False)
    if left or right or up or down:
        return True
    else:
        return False


for yt in range(1, len(lines) - 1):
    for xt in range(1, len(lines[0]) - 1):
        visible += 1 if check_if_visible(xt, yt) else 0
        
print("Part One: {}".format(visible))

# ----------------------------------------------------------------------------------------------------

def get_single_direction_score(x: int, y: int, to_max: bool, x_direction: bool) -> int:
    height = int(lines[y][x])
    s = 0
    if x_direction:
        while x < x_max if to_max else x > 0:
            x += 1 if to_max else -1
            s += 1
            if int(lines[y][x]) >= height:
                break
        return s
    else:
        while y < y_max if to_max else y > 0:
            y += 1 if to_max else -1
            s += 1
            if int(lines[y][x]) >= height:
                break
        return s
    

def get_scenic_score(x: int, y: int):
    left = get_single_direction_score(x, y, to_max=False, x_direction=True)
    right = get_single_direction_score(x, y, to_max=True, x_direction=True)
    up = get_single_direction_score(x, y, to_max=False, x_direction=False)
    down = get_single_direction_score(x, y, to_max=True, x_direction=False)
    
    return left * right * up * down

score = 0
for yt in range(1, len(lines) - 1):
    for xt in range(1, len(lines[0]) - 1):
        score = max(score, get_scenic_score(xt, yt))
            
print("Part Two: {}".format(score))