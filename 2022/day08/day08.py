from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

lines = file.read().split("\n")

def check_single_direction_visible(x: int, y: int, max: int, from_max: bool, x_direction: bool) -> bool:
    """Check if tree will be visible in a given direction (every height in row/column smaller than own height)

    Args:
        x (int): x of tree
        y (int): y of tree
        max (int): max of index in given direction
        from_max (bool): Check visibility from max or min index to tree
        x_direction (bool): Check in x or y direction

    Returns:
        bool: If tree is visible in specified direction
    """
    height = int(lines[y][x])
    if x_direction:
        initial = x
        x = max if from_max else 0
        while x > initial if from_max else x < initial:
            if int(lines[y][x]) >= height:
                break
            x += -1 if from_max else 1
            if x == initial:
                return True
        return False
    else:
        initial = y
        y = max if from_max else 0
        while y > initial if from_max else y < initial:
            if int(lines[y][x]) >= height:
                break
            y += -1 if from_max else 1
            if y == initial:
                return True
        return False

x_max, y_max = len(lines[0]) - 1, len(lines) - 1	# index maxima
def check_if_visible(x: int, y: int) -> bool:
    """Check if tree is visible from any direction

    Args:
        x (int): x of tree
        y (int): y of tree

    Returns:
        bool: If tree is visible from any direction
    """
    left = check_single_direction_visible(x, y, x_max, from_max=False, x_direction=True)
    right = check_single_direction_visible(x, y, x_max, from_max=True, x_direction=True)
    up = check_single_direction_visible(x, y, y_max, from_max=False, x_direction=False)
    down = check_single_direction_visible(x, y, y_max, from_max=True, x_direction=False)
    if left or right or up or down:
        return True
    else:
        return False

visible = 2 * len(lines[0]) + 2 * len(lines) - 4	# outer trees
for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        visible += 1 if check_if_visible(x, y) else 0
        
print("Part One: {}".format(visible))

# ----------------------------------------------------------------------------------------------------

def get_single_direction_score(x: int, y: int, max_index: int, to_max: bool, x_direction: bool) -> int:
    """Check scenic score of tree in a given direction

    Args:
        x (int): x of tree
        y (int): y of tree
        max_index (int): max of index in the given direction
        to_max (bool): Check scenic score in direction of max of min index
        x_direction (bool): Check in x or y direction

    Returns:
        int: Scenic score for the specified direction
    """
    height = int(lines[y][x])
    s = 0
    if x_direction:
        while x < max_index if to_max else x > 0:
            x += 1 if to_max else -1
            s += 1
            if int(lines[y][x]) >= height:
                break
        return s
    else:
        while y < max_index if to_max else y > 0:
            y += 1 if to_max else -1
            s += 1
            if int(lines[y][x]) >= height:
                break
        return s
    
def get_scenic_score(x: int, y: int) -> int:
    """Gets the total scenic score for a tree

    Args:
        x (int): x of tree
        y (int): y of tree

    Returns:
        int: Total scenic score of given tree
    """
    left = get_single_direction_score(x, y, x_max, to_max=False, x_direction=True)
    right = get_single_direction_score(x, y, x_max, to_max=True, x_direction=True)
    up = get_single_direction_score(x, y, y_max, to_max=False, x_direction=False)
    down = get_single_direction_score(x, y, y_max, to_max=True, x_direction=False)
    
    return left * right * up * down

score = 0
for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        score = max(score, get_scenic_score(x, y))
            
print("Part Two: {}".format(score))