outcome = ["BX", "CY", "AZ", "AX", "BY", "CZ", "CX", "AY", "BZ"]
outcome2 = ["BX", "CX", "AX", "AY", "BY", "CY", "CZ", "AZ", "BZ"]

with open("data/day02.txt", "r") as file:
    data = [x.strip().replace(" ", "") for x in file.readlines()]

score = 0
score2 = 0
for duel in data:
    score += outcome.index(duel) + 1
    score2 += outcome2.index(duel) + 1

print("Part 1:", score)
print("Part 2:", score2)
