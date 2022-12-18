from itertools import zip_longest
from functools import cmp_to_key


def compare(left, right):
    if left is None:
        return -1
    if right is None:
        return 1

    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return -1
        elif left > right:
            return 1
        else:
            return 0
    elif isinstance(left, list) and isinstance(right, list):
        for l, r in zip_longest(left, right):
            if (result := compare(l, r)) != 0:
                return result
        return 0
    else:
        l = [left] if isinstance(left, int) else left
        r = [right] if isinstance(right, int) else right
        return compare(l, r)


data = [
    list(map(eval, pair.split("\n")))
    for pair in [
        pack.strip() for pack in open("data/day13.txt", "r").read().split("\n\n")
    ]
]
all_packs = [item for sublist in data for item in sublist]

good_order = []
for i, entry in enumerate(data):
    left, right = entry
    if compare(left, right) < 0:
        good_order.append(i + 1)

print("Part 1:", sum(good_order))
div1, div2 = [[2]], [[6]]
sorted_packs = sorted([*all_packs, div1, div2], key=cmp_to_key(compare))
print("Part 2:", (sorted_packs.index(div1) + 1) * (sorted_packs.index(div2) + 1))
