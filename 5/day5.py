def calculate_seat(line):
    rows = [i for i in range(0, 128)]
    cols = [i for i in range(0, 8)]
    
    row_alg = line[0:7]
    col_alg = line[7:10]
    
    for c in row_alg:
        if c == "F":
            rows = rows[:len(rows)//2]
        elif c == "B":
            rows = rows[len(rows)//2:]

    for c in col_alg:
        if c == "L":
            cols = cols[:len(cols)//2]
        elif c == "R":
            cols = cols[len(cols)//2:]
    
    return rows[0] * 8 + cols[0]

max_id = 0
ids = []
with open("5/input.txt", "r") as in_file:
    for line in in_file.readlines():
        ids.append(calculate_seat(line))

ids.sort()

for i in range(0, len(ids) - 1):
    if ids[i] != ids[i + 1] - 1:
        print(str(ids[i + 1] - 1))

