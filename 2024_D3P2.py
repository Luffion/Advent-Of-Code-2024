import re

with open("data.txt", "r") as f:
    lines = f.readline()

instructions = []

valid_data = re.findall(r"mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", lines)

valid = True

for data in valid_data:
    if data == "do()":
        valid = True
    elif data == "don't()":
        valid = False

    if valid and data != "do()" and data != "don't()":
        instructions.append(data)

sum = 0
for instruction in instructions:
    num1, num2 = instruction[4:-1].split(",")
    sum += int(num1) * int(num2)
print(sum)
