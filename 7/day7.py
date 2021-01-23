import re

# Part 1
bags = {}
with open("7/input.txt", "r") as in_file:
    rules = in_file.readlines()
    for line in rules:
        match = re.findall( "(\w+ \w+) bag", line)
        bags[match[0]] = [group for group in match[1:]]

seen = []
def find_containing_bags(bag_name):
    total = 0
    for k, v in bags.items():
        if bag_name in v and k not in seen:
            total += 1
            total += find_containing_bags(k)
            seen.append(k)

    return total

print(str(find_containing_bags("shiny gold")))

# Part 2
bags = {}
with open("7/input.txt", "r") as in_file:
    rules = in_file.readlines()
    for line in rules:
        key = re.search( "(\w+ \w+) bags contain", line)
        contains = re.findall("(\d) (\w+ \w+) bag", line)

        if len(contains) > 0:
            bags[key.group(1)] = {bag[1]: int(bag[0]) for bag in contains}
        
def find_number_of_contained_bags(bag_name):
    total = 0
    if bag_name not in bags.keys():
        return 0
    for k, v in bags[bag_name].items():
        total += v + v * find_number_of_contained_bags(k)
    return total

print(str(find_number_of_contained_bags("shiny gold")))
