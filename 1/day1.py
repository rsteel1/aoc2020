nums = []

with open("1/input.txt", "r") as in_file:
    for line in in_file.readlines():
        nums.append(int(line.strip()))


nums.sort()
size = len(nums)
for i in nums:
    for j in nums:
        for k in nums:
            if i + j + k == 2020:
                print(i * j * k)
    nums.remove(i)
