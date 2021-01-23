
# Part 1
groups = []
with open("6/input.txt", "r") as in_file:
    group = []
    for line in in_file.readlines():
        if line == "\n":
            groups.append(group)
            group = []
        else:
            for char in line.strip("\n"):
                group.append(char)

total = 0
for group in groups:
    unique = set(group)
    total += len(unique)

print(total)

# Part 2
groups = []
with open("6/input.txt", "r") as in_file:
    group = []
    for line in in_file.readlines():
        if line == "\n":
            groups.append(group)
            group = []
        else:
            group.append(line.strip("\n"))

total = 0
for group in groups:
    answers = {}
    for answer in group:
        for c in answer:
            if c not in answers.keys():
                answers[c] = 1
            else:
                answers[c] += 1

    for k, v in answers.items():
        if v == len(group):
            total += 1

print(total)