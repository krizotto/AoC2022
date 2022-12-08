with open("data/day01.txt", "r") as file:
    data = sorted(
        [
            sum(x)
            for x in [
                [int(cal) for cal in elf.split("\n")]
                for elf in file.read().split("\n\n")
            ]
        ],
        reverse=True,
    )

print("Part 1:", data[0])
print("Part 2:", data[0] + data[1] + data[2])
