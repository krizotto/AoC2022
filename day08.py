from collections import defaultdict


def check_tree(x: int, y: int):
    tmp_score = 1
    current_height = grid[(x, y)][0]
    is_visible = False
    tmp_bool, score = check_left(x, y, current_height)
    is_visible |= tmp_bool
    tmp_score *= score
    tmp_bool, score = check_right(x, y, current_height)
    is_visible |= tmp_bool
    tmp_score *= score
    tmp_bool, score = check_up(x, y, current_height)
    is_visible |= tmp_bool
    tmp_score *= score
    tmp_bool, score = check_down(x, y, current_height)
    is_visible |= tmp_bool
    tmp_score *= score
    return is_visible, tmp_score


def check_left(x: int, y: int, height: int):
    tmp_bool = True
    last_highest_index = 0
    for i in range(x):
        if grid[(i, y)][0] >= height:
            tmp_bool = False
            last_highest_index = i
    return tmp_bool, x - last_highest_index


def check_right(x: int, y: int, height: int):
    for i in range(x + 1, x_max):
        if grid[(i, y)][0] >= height:
            return False, i - x
    return True, x_max - x - 1


def check_up(x: int, y: int, height: int):
    tmp_bool = True
    last_highest_index = 0
    for i in range(y):
        if grid[(x, i)][0] >= height:
            tmp_bool = False
            last_highest_index = i
    return tmp_bool, y - last_highest_index


def check_down(x: int, y: int, height: int):
    for i in range(y + 1, y_max):
        if grid[(x, i)][0] >= height:
            return False, i - y
    return True, y_max - y - 1


data = [list(map(int, list(x.strip()))) for x in open("data/day08.txt", "r")]
y_max = len(data)
x_max = len(data[0])
grid = defaultdict(int)
sum_visible = 0
scores = []

for y in range(y_max):
    for x in range(x_max):
        grid[(x, y)] = (data[y][x], False)

for y in range(y_max):
    for x in range(x_max):
        is_visible, score = check_tree(x, y)
        scores.append(score)
        sum_visible += is_visible
        grid[(x, y)] = (data[y][x], is_visible, score)


print("Part 1:", sum_visible)
print("Part 2:", max(scores))
