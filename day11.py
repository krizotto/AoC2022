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
        new = math.floor(eval(self.function) / 3)
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
monkeys = [
    Monkey([79, 98], "old*19", 23, 2, 3),
    Monkey([54, 65, 75, 74], "old+6", 19, 2, 0),
    Monkey([79, 60, 97], "old*old", 13, 1, 3),
    Monkey([74], "old+3", 17, 0, 1),
]

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

for i in range(len(monkeys)):
    print("Monkey", i, "inspected items", monkeys[i].get_inspected_items(), "times.")

# print(data)
# new = 0
# old = 1
# new = eval("old + 1")
# print(new, old)
