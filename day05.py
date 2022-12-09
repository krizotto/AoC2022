from copy import deepcopy
from re import split, findall


def prepare_input_stacks(input_stacks):
    riddle_input = ""
    # Prepare stacks
    # Add spaces in the end of each line of input_stacks
    for i in input_stacks.split("\n"):
        riddle_input += i + " "
    riddle_input = findall("....", riddle_input)
    max_column = int(riddle_input[-1])

    # Prepare stacks
    stacks_top_to_bottom = []
    stacks_bottom_to_top = []
    for i in range(max_column):
        stacks_top_to_bottom.append([])
    # Fill in stacks
    for i in range(len(riddle_input)):
        stacks_top_to_bottom[i % max_column].append(
            riddle_input[i].strip().replace("[", "").replace("]", "")
        )
    # Reverse stacks and save as bottom_to_top
    for stack in stacks_top_to_bottom:
        stack.pop()
        stack = list(filter(None, stack))
        stack.reverse()
        stacks_bottom_to_top.append(stack)
    return stacks_bottom_to_top


# Prepare instructions
def prepare_input_instructions(instructions):
    return [
        list(map(int, list(filter(None, split("move|from|to| ", x)))))
        for x in instructions.strip().split("\n")
    ]


input_stacks, instructions = "".join(
    [x for x in open("data/day05.txt", "r").read()]
).split("\n\n")

stacks_bottom_to_top = prepare_input_stacks(input_stacks)
instructions = prepare_input_instructions(instructions)

stacks_part1 = deepcopy(stacks_bottom_to_top)
stacks_part2 = deepcopy(stacks_bottom_to_top)

for amount, stack_from, stack_to in instructions:
    temp_list = []
    for i in range(amount):
        stacks_part1[stack_to - 1].append(stacks_part1[stack_from - 1].pop())
        temp_list.append(stacks_part2[stack_from - 1].pop())
    for i in range(amount):
        stacks_part2[stack_to - 1].append(temp_list.pop())


part1 = ""
part2 = ""
for stack in stacks_part1:
    part1 += stack[-1]
for stack in stacks_part2:
    part2 += stack[-1]
print("Part 1:", part1)
print("Part 2:", part2)
