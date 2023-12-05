from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

lines = lines = file.read().split("\n")

digit_array = list()

def first_digit(line):
    for c in line:
        if '0' <= c <= '9':
            return int(c)

for line in lines:
    new_line = []
    
    digit_array.append(first_digit(line) * 10 + first_digit(line[::-1]))
    
print("Part One: {}".format(sum(digit_array)))

num_dict = {
    "z": {"zero": 0},
    "o": {"one": 1},
    "t": {"two": 2, "three": 3},
    "f": {"four": 4, "five": 5},
    "s": {"six": 6, "seven": 7},
    "e": {"eight": 8},
    "n": {"nine": 9}
}

digit_array.clear()

for line in lines:
    tokens = list()
    for i in range(len(line)):
        if '0' <= line[i] <= '9':
            tokens.append(int(line[i]))
        elif line[i] in num_dict.keys():
            for key in num_dict[line[i]]:
                if line[i::].startswith(key):
                    tokens.append(num_dict[line[i]][key])
        
    digit_array.append(int(tokens[0]) * 10 + int(tokens[-1]))
    
print("Part Two: {}".format(sum(digit_array)))