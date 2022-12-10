from collections import defaultdict


def add_value():
    global x, value_to_add
    x += value_to_add.pop()


def hold(value):
    global should_wait, value_to_add
    value_to_add.append(value)
    should_wait = True


def release():
    global should_wait
    should_wait = False


instructions = iter([x.strip() for x in open("data/day10.txt", "r").readlines()])
signal_strengths = defaultdict(int)
value_to_add = []
x = 1
should_wait = False

for i in range(1, 300):
    if should_wait:
        signal_strengths[i] = x
        release()
    else:
        if len(value_to_add) > 0:
            add_value()
        signal_strengths[i] = x
        instruction = next(instructions, None)
        if instruction == None:
            break
        elif instruction.startswith("noop"):
            continue
        else:
            hold(int(instruction.split()[1]))

signal_sum = 0
for i in range(20, 221, 40):
    signal_sum += signal_strengths[i] * i

print("Part 1:", signal_sum)
print("Part 2:")
for k, v in signal_strengths.items():
    if (k - 1) % 40 == 0:
        print("\n")
    if (k - 1) % 40 in [v - 1, v, v + 1]:
        print("###", end="")
    else:
        print("   ", end="")
