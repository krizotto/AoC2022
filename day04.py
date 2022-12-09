data = [
    [x.split("-"), y.split("-")]
    for x, y in [z.split(",") for z in [x.strip() for x in open("data/day04.txt", "r")]]
]
count_intersections = 0
count_includes = 0
for pair in data:
    pair = [[int(a), int(b)] for a, b in pair]
    range_a = set(range(pair[0][0], pair[0][1] + 1))
    range_b = set(range(pair[1][0], pair[1][1] + 1))
    if range_a.issubset(range_b) or range_b.issubset(range_a):
        count_includes += 1
    if range_a & range_b:
        count_intersections += 1

print("Part 1:", count_includes)
print("Part 2:", count_intersections)
