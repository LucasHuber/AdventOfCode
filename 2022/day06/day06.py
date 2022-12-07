from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

line = file.read().replace("\n", "")
numb = 0

# String indexing Example: <str>[i(inclusive):j(exclusive)]

for i in range(4, len(line)):
    if (len(set(line[i-4:i])) == 4):
        numb = i
        break
    
print("Part One: {}".format(numb))

for i in range(14, len(line)):
    if (len(set(line[i-14:i])) == 14):
        numb = i
        break
    
print("Part Two: {}".format(numb))