with open("data.txt", "r") as f:
    reports = [list(map(int, line.strip().split())) for line in f if line.strip()]

def is_safe(report):
    pointer = 1
    if report[pointer] - report[pointer-1] == 0:
        return False
    status = (report[pointer] - report[pointer-1]) / abs(report[pointer] - report[pointer-1])

    while pointer < len(report):
        if report[pointer] > report[pointer-1]:
            if status != 1:
                return False
        else:
            if status != -1:
                return False
        if abs(report[pointer] - report[pointer - 1]) < 1 or abs(report[pointer] - report[pointer - 1]) > 3:
            return False
        pointer += 1

    return True

sum = 0
for report in reports:
    if is_safe(report):
        sum += 1
print(sum)
