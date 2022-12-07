from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

current_path = ""
tree_view = {}

def add_size_to_dir_and_subdir(size : int, path : str):
    while(path != "/"):
        add_size_to_dir(size, path)
        path = remove_last_dir(path)
    add_size_to_dir(size, path)

def add_size_to_dir(size : int, path : str):
    tree_view[path] += size
    pass

def remove_last_dir(path : str) -> str:
    path = "/".join(path.split("/")[:-1])
    return "/" if len(path) == 0 else path

lines = file.read().split("\n")

for line in lines:
    dirs = []
    match line.split(" "):
        case ["$", "cd", "/"]:
            current_path = "/"
            tree_view[current_path] = 0
        case ["$", "cd", ".."]:
            current_path = remove_last_dir(current_path)
        case ["$", "cd", name]:
            current_path += "/" + name if current_path != "/" else name
            tree_view[current_path] = 0
        case ["$", "ls"]:
            pass
        case ["dir", name]:
            pass
        case [size, name]:
            add_size_to_dir_and_subdir(int(size), current_path)

solution_one = sum(v for v in tree_view.values() if v <= 100000)
print("Part One: {}".format(solution_one))

total_used = tree_view["/"]
wanted = 70000000 - 30000000
needed = total_used - wanted

solution_two = min(v for v in tree_view.values() if v > needed)            
print("Part Two: {}".format(solution_two))