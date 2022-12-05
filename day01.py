with open("data/day01.txt", "r") as file:
    data = [[int(cal) for cal in elf.split("\n")] for elf in file.read().split("\n\n")]

elvesWithCalories = sorted([sum(x) for x in data], reverse=True)

print("Part 1:", elvesWithCalories[0])
print("Part 2:", elvesWithCalories[0] + elvesWithCalories[1] + elvesWithCalories[2])
