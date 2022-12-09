from collections import defaultdict


def check_tree(x: int, y: int) -> bool:
    current_height = grid[(x, y)][0]
    is_visible = False
    is_visible |= check_left(x, y, current_height)
    is_visible |= check_right(x, y, current_height)
    is_visible |= check_up(x, y, current_height)
    is_visible |= check_down(x, y, current_height)
    return is_visible


def check_left(x: int, y: int, current_height: int) -> bool:
    for i in range(x):
        if grid[(i, y)][0] >= current_height:
            return False
    return True


def check_right(x: int, y: int, current_height: int) -> bool:
    for i in range(x + 1, x_max):
        if grid[(i, y)][0] >= current_height:
            return False
    return True


def check_up(x: int, y: int, current_height: int) -> bool:
    for i in range(y):
        if grid[(x, i)][0] >= current_height:
            return False
    return True


def check_down(x: int, y: int, current_height: int) -> bool:
    for i in range(y + 1, y_max):
        if grid[(x, i)][0] >= current_height:
            return False
    return True


data = [list(map(int, list(x.strip()))) for x in open("data/day08.txt", "r")]
y_max = len(data)
x_max = len(data[0])
grid = defaultdict(int)
sum_visible = 0

# Fill grid
for y in range(y_max):
    for x in range(x_max):
        grid[(x, y)] = (data[y][x], False)

for y in range(y_max):
    for x in range(x_max):
        is_visible = check_tree(x, y)
        sum_visible += is_visible
        grid[(x, y)] = (data[y][x], is_visible)
    #     print(int(is_visible), end=" ")
    # print("\n")


print("Part 1:", sum_visible)
