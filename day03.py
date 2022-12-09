def find_common_part_1(a: str, b: str) -> int:
    a_set = set(list(a))
    b_set = set(list(b))
    return letters.index(next(iter(a_set & b_set)))


def find_common_part_2(a: str, b: str, c: str) -> int:
    a_set = set(list(a))
    b_set = set(list(b))
    c_set = set(list(c))
    return letters.index(next(iter(a_set & b_set & c_set)))


data = [x.strip() for x in open("data/day03.txt", "r")]
letters = list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
rucksacks = [(x[: len(x) // 2], x[len(x) // 2 :]) for x in data]
sum_a = 0
sum_b = 0
for rucksack in data:
    sum_a += find_common_part_1(
        rucksack[: len(rucksack) // 2], rucksack[len(rucksack) // 2 :]
    )

for i in range(0, len(data), 3):
    sum_b += find_common_part_2(data[i], data[i + 1], data[i + 2])

print("Part 1:", sum_a)
print("Part 2:", sum_b)
