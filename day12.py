from collections import defaultdict

# parse data to (x,y)->value dict
def extract_map(data):
    input_map = defaultdict(str)

    for y, line in enumerate(data):
        for x, letter in enumerate(line):
            input_map[(x, y)] = letter
    return input_map


def get_map_sizes(input_map):
    max_x, max_y = [1 + elem for elem in list(input_map)[-1]]
    return max_x, max_y


def find_start_and_end(input_map: defaultdict):
    start, end = (0, 0), (0, 0)
    for k, v in input_map.items():
        if v == "S":
            start = k
        if v == "E":
            end = k

    return start, end


data = [x.strip() for x in open("data/test-day12.txt", "r").readlines()]
input_map = extract_map(data)
max_x, max_y = get_map_sizes(input_map)
start, end = find_start_and_end(input_map)


print(start, end)
