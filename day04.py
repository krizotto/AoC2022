import re


def solution(a, b, c, d):
    global count_includes
    global count_intersections
    a_set = set(range(a, b + 1))
    b_set = set(range(c, d + 1))
    if a_set.issubset(b_set) or b_set.issubset(a_set):
        count_includes += 1
    if a_set & b_set:
        count_intersections += 1


count_intersections = 0
count_includes = 0
[
    solution(int(a), int(b), int(c), int(d))
    for a, b, c, d in [
        re.split("[-,]", z) for z in [x.strip() for x in open("data/day04.txt", "r")]
    ]
]

print("Part 1:", count_includes)
print("Part 2:", count_intersections)
