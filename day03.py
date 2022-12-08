def find_common(rucksack):
    a, b = rucksack
    # TODO: prepare algorithm
    return "a"


data = [x.strip() for x in open("data/test-day03.txt", "r")]
rucksacks = [(x[: len(x) // 2], x[len(x) // 2 :]) for x in data]
output = []
for rucksack in rucksacks:
    first, second = rucksack
    output.append(find_common(rucksack))

# TODO: replace letters with numbers
print(output)
