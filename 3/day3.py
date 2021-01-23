import pprint

pp = pprint.PrettyPrinter()

# # Part 1
# with open("3/input.txt", "r") as in_file:
#     position = 0
#     trees = 0
#     for line in in_file:
#         max_pos = len(line) - 1
#         if line[position] == "#":
#             trees += 1
#         position = (position + 3) % max_pos
    # print(trees)

# Part 2
def count_trees(in_lines, slope_x, slope_y):
    position = trees = 0
    for i, line in enumerate(in_lines):
        line = line.strip()
        max_pos = len(line)
        if i % slope_y == 0:
            if line[position] == "#":
                trees += 1
            position = (position + slope_x) % max_pos
        
    return trees
    
with open("3/input.txt", "r") as in_file:
    lines = in_file.readlines()
    accumulator = 1

    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slopes:
        accumulator *= count_trees(lines, slope[0], slope[1])

    print(f"Accumulator: {accumulator}")