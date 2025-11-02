import re

with open("data.txt", "r") as f:
    lines = f.readline()

instructions = re.findall(r"mul\([0-9]+,[0-9]+\)", lines)

print(instructions)

sum = 0
for instruction in instructions:
    num1, num2 = instruction[4:-1].split(",")
    sum += int(num1) * int(num2)
print(sum)
