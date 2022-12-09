def move(direction, amount):
    for _ in range(amount):
        x_h, y_h = h_pos[-1]
        fix_x = False
        fix_y = False
        x_increment, y_increment = 0, 0
        if direction == "R":
            x_increment = 1
            fix_y = True
        elif direction == "L":
            x_increment = -1
            fix_y = True
        elif direction == "U":
            y_increment = -1
            fix_x = True
        elif direction == "D":
            y_increment = 1
            fix_x = True

        h_pos.append((x_h + x_increment, y_h + y_increment))

        if not touch():
            move_t(x_h, y_h, x_increment, y_increment, fix_x, fix_y)


def move_t(x_h, y_h, x_increment, y_increment, fix_x, fix_y):
    x_t, y_t = t_pos[-1]
    if fix_x:
        t_pos.append((x_h + x_increment, y_t + y_increment))
    elif fix_y:
        t_pos.append((x_t + x_increment, y_h + y_increment))


def touch() -> list():
    x, y = t_pos[-1]
    possible_places_for_h = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            possible_places_for_h.append((x + j, y + i))
    return possible_places_for_h.count(h_pos[-1])


data = [
    (a, int(b))
    for a, b in [x.strip().split() for x in open("data/day09.txt", "r").readlines()]
]

h_pos = [(0, 0)]
t_pos = [(0, 0)]
for direction, amount in data:
    move(direction, amount)

print("Part 1:", len(set(t_pos)))
