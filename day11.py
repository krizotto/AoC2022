import math
from copy import deepcopy


class Monkey:
    def __init__(
        self, items, function: str, test: int, if_true: int, if_false: int
    ) -> None:
        self.items = items
        self.if_true = if_true
        self.if_false = if_false
        self.function = function
        self.test = test
        self.items_to_throw = []
        self.inspected_items = 0

    def process_round(self):
        self.items.reverse()
        for _ in range(len(self.items)):
            self.inspect_item(self.items.pop())
        return self.throw()

    def inspect_item(self, old):
        self.inspected_items += 1
        if divide_by == 1:
            new = eval(self.function)
        else:
            new = math.floor(eval(self.function) / divide_by)
        if new % self.test == 0:
            self.items_to_throw.append((self.if_true, new))
        else:
            self.items_to_throw.append((self.if_false, new))

    def catch_item(self, worry_level):
        self.items.append(worry_level)

    def throw(self):
        return_items = deepcopy(self.items_to_throw)
        self.items_to_throw = []
        return return_items

    def get_inspected_items(self):
        return self.inspected_items


max_rounds = 20
divide_by = 3
monkeys = [
    Monkey([57], "old*13", 11, 3, 2),
    Monkey([58, 93, 88, 81, 72, 73, 65], "old+2", 7, 6, 7),
    Monkey([65, 95], "old+6", 13, 3, 5),
    Monkey([58, 80, 81, 83], "old*old", 5, 4, 5),
    Monkey([58, 89, 90, 96, 55], "old+3", 3, 1, 7),
    Monkey([66, 73, 87, 58, 62, 67], "old*7", 17, 4, 1),
    Monkey([85, 55, 89], "old+4", 2, 2, 0),
    Monkey([73, 80, 54, 94, 90, 52, 69, 58], "old+7", 19, 6, 0),
]
monkeys_p2 = deepcopy(monkeys)


def solution(max_rounds, monkeys):
    items_to_throw = []
    for _ in range(max_rounds):
        for i in range(len(monkeys)):
            for item in [item for item in items_to_throw if item[0] is i]:
                monkeys[item[0]].catch_item(item[1])
            items_to_throw = [item for item in items_to_throw if item[0] is not i]
            processed = monkeys[i].process_round()
            if len(processed) > 0:
                items_to_throw.extend(processed)
        for item in items_to_throw:
            monkeys[item[0]].catch_item(item[1])
        items_to_throw = []

    inspected_list = []
    for monkey in monkeys:
        inspected_list.append(monkey.get_inspected_items())

    for i in range(len(monkeys)):
        print("Monkey", i, "inspected items", inspected_list[i], "times.")

    inspected_list = sorted(inspected_list, reverse=True)
    print("Monkey business:", inspected_list[0] * inspected_list[1])


print("Part 1:")
solution(20, monkeys)
# TODO: Change managing swaps states - stuck at about 540 of 10000
# divide_by = 1
# print("Part 2:")
# solution(10000, monkeys_p2)
