from pprint import PrettyPrinter
pp = PrettyPrinter()

# Part 1
passports = list()
passport = {}

def validate_data(passport: dict):
    try:
        # Birth year
        byr = int(passport["byr"])
        if byr < 1920 or byr > 2002:
            return False

        # Issue year
        iyr = int(passport["iyr"])
        if iyr < 2010 or iyr > 2020:
            return False

        # Expiration
        eyr = int(passport["eyr"])
        if eyr < 2020 or eyr > 2030:
            return False
        
        # Height
        height = passport["hgt"]
        height_n = int(height[:-2])
        if height[-2:] == "cm":
            if height_n < 150 or height_n > 193:
                return False
        elif height[-2:] == "in":
            if height_n < 59 or height_n > 76:
                return False
        else:
            return False
        
        # Hair colour
        colour = passport["hcl"]
        if colour[0] != "#" or len(colour) != 7:
            return False

        for c in colour[1:]:
            if c not in "1234567890abcdef":
                return False

        print("Checking eye colour")
        if passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            print("eye colour invalid")
            return False

        print("checking pid")
        if len(passport["pid"]) != 9:
            print("pid invalid")
            return False

        for c in passport["pid"]:
            if not c.isdigit():
                print("pid invalid")
                return False

        return True

    except Exception as e:
        print(str(e))
        return False

with open("4/input.txt", "r") as in_file:
    for line in in_file.readlines():        
        if line == "\n":
            passports.append(passport)
            passport = {}
            continue

        fields = line.split(" ")
        for field in fields:
            vals = field.strip().split(":")
            if vals[0] in passport.keys():
                passport["valid"] = False
            passport[vals[0]] = vals[1]

required = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid") # "cid"

count = 0
for passport in passports:
    valid = validate_data(passport)
    if valid:
        count += 1

# passport = {
#     "hcl": "#733820",
#     "ecl": "brn",
#     "byr": "2000",
#     "eyr": "2022",
#     "iyr": "2014",
#     "cid": "320",
#     "pid": "851634349",
#     "hgt": "180cm"
# }

# print(validate_data(passport))

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.

print(count)