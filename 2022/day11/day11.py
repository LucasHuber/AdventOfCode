from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

from Monkey import Monkey

lines = file.read().split("\n")

monkey_items = []
monkey_list = []

for line in lines:
    if line.startswith("Monkey"):
        monkey_index = int(line.split(" ")[1].replace(":", ""))
        continue
    if line.strip().startswith("Starting"):
        items = [int(item) for item in line.split(": ")[1].split(", ")]
        continue
    if line.strip().startswith("Operation"):
        op = line.split("= ")[1].split(" ")
        match (op):
            case ["old", "+", value]:
                worry_operator = "add"
                worry_value = 0 if value == "old" else int(value)
            case ["old", "*", value]:
                worry_operator = "times"
                worry_value = 0 if value == "old" else int(value)
        continue
    if line.strip().startswith("Test"):
        test_against = int(line.split(" ")[-1])
        continue
    if line.strip().startswith("If true"):
        true_target = int(line.split(" ")[-1])
        continue
    if line.strip().startswith("If false"):
        false_target = int(line.split(" ")[-1])
        continue
    if line == "":
        monkey_list.append(Monkey(monkey_items, monkey_index, items, worry_operator, 
                                  worry_value, test_against, 0, true_target, false_target))

lcm = monkey_list[0].test_against
for monkey in monkey_list[1:]:
    lcm = monkey.test_against * lcm 

for monkey in monkey_list:
    monkey.lcm = lcm
    
for _ in range(10000):          # 20 for Part One, 10000 for Part Two
    for monkey in monkey_list:
        monkey.inspect()
        
for monkey in monkey_list:
    print(f"Monkey {monkey.monkey_index} inspected {monkey.items_inspected} items.")
    
inspected_numbers = [monkey.items_inspected for monkey in monkey_list]
inspected_numbers.sort(reverse=True)
print("Part Solution: {}".format(inspected_numbers[0] * inspected_numbers[1]))
