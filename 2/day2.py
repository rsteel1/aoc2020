count = 0

def get_data(line: str):
    return line.replace(": ", " ").replace("-", " ").strip().split(" ")

# Part 1
with open("2/input.txt", "r") as in_file:
    for line in in_file:
        data = get_data(line)

        min = int(data[0])
        max = int(data[1])
        target = data[2]
        password = data[3]

        if min <= password.count(target) <= max:
            count += 1

print(f"Part 1 Valid Passwords: {count}")

# Part 2
count = 0
with open("2/input.txt", "r") as in_file:
    for line in in_file:
        data = get_data(line)
        
        pos1 = int(data[0]) - 1
        pos2 = int(data[1]) - 1
        target = data[2]
        password = data[3]

        if (password[pos1] == target and password[pos2] != target) or (password[pos1] != target and password[pos2] == target):
            count += 1

print(f"Part 2 Valid Passwords: {count}")