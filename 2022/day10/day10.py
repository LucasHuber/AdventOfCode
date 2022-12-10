from os import path
file = open(path.join(path.dirname(__file__), "input.txt"))

lines = file.read().split("\n")

cycle = 0
x_reg = 1
signal_strength = 0

def check_for_signal_strength():
    global signal_strength
    if cycle == 20 or ((cycle - 20) % 40 == 0):
        signal_strength += x_reg * cycle

for line in lines:
    match (line.split(" ")):
        case ["noop"]:
            cycle += 1
            check_for_signal_strength()
        case ["addx", val]:
            val = int(val)
            cycle += 1
            check_for_signal_strength()
            cycle += 1
            check_for_signal_strength()
            x_reg += val

print("Part One: {}".format(signal_strength))

# ----------------------------------------------------------------------------------------------------

cycle = 0
x_reg = 1               # sprite middle position
crt_position = 0
rows, cols = (6, 40)
screen = [["." for _ in range(cols)] for _ in range(rows)]

in_sprite = lambda x: x >= x_reg - 1 and x <= x_reg + 1

def process_crt():
    global crt_position
    if (in_sprite(crt_position)):
        screen[cycle // 40][crt_position] = "#"
    crt_position = crt_position + 1 if crt_position < 39 else 0
    
for line in lines:
    match (line.split(" ")):
        case ["noop"]:
            process_crt()
            cycle += 1
        case ["addx", val]:
            val = int(val)
            process_crt()
            cycle += 1
            process_crt()
            cycle += 1
            x_reg += val
            
print("Part Two:")
for row in screen:
    print("".join(row))