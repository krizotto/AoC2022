from re import split

# for tests:
# stacks = [["Z", "N"], ["M", "C", "D"], ["P"]]
stacks = [
    list("FHBVRQDP"),
    list("LDZQWV"),
    list("HLZQGRPC"),
    list("RDHFJVB"),
    list("ZWLC"),
    list("JRPNTGVM"),
    list("JRLVMBS"),
    list("DPJ"),
    list("DCNWV"),
]
stacks_part2 = [
    list("FHBVRQDP"),
    list("LDZQWV"),
    list("HLZQGRPC"),
    list("RDHFJVB"),
    list("ZWLC"),
    list("JRPNTGVM"),
    list("JRLVMBS"),
    list("DPJ"),
    list("DCNWV"),
]


data = [x.strip() for x in open("data/day05.txt", "r").readlines()]
instructions = [
    list(map(int, list(filter(None, split("move|from|to| ", x)))))
    for x in data[data.index("") + 1 :]
]

for amount, fromm, to in instructions:
    temp_list = []
    for i in range(amount):
        stacks[to - 1].append(stacks[fromm - 1].pop())
        temp_list.append(stacks_part2[fromm - 1].pop())
    for i in range(amount):
        stacks_part2[to - 1].append(temp_list.pop())


part1 = ""
part2 = ""
for stack in stacks:
    part1 += stack[-1]
for stack in stacks_part2:
    part2 += stack[-1]
print(part1)
print(part2)
