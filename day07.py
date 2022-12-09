from collections import defaultdict


data = [x.strip() for x in open("data/day07.txt", "r").readlines()]
current_directory = []
directories_sizes = defaultdict(int)
max_size = 100000
total_size = 0

for line in data:
    if line.startswith("$ cd"):
        directory = line.split()[-1]
        if directory == "..":
            current_directory.pop()
        else:
            current_directory.append(directory)
    elif line.startswith("$ ls"):
        # proceed to next line to count sizes
        continue
    else:
        size, file = line.split()
        if size.isdigit():
            size = int(size)
            for depth in range(len(current_directory)):
                directories_sizes["/".join(current_directory[: depth + 1])] += size

for k, v in directories_sizes.items():
    if v <= max_size:
        total_size += v

print("Part 1:", total_size)
space_to_be_freed = 30000000 - (70000000 - directories_sizes["/"])
new_sizes = sorted(directories_sizes.items(), key=lambda kv: kv[1])

for k, v in new_sizes:
    if v >= space_to_be_freed:
        print("Part 2:", v)
        break
