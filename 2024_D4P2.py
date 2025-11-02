with open("data.txt", "r") as f:
    letters = [list(line.strip()) for line in f]

def cross_check(row, col):
    sum = 0
    for i in range(-1, 2, 2):
        for j in range(-1, 2, 2):
            if letters[row+i][col+j] == "M" and letters[row-i][col-j] == "S":
                sum += 1
    if sum == 2:
        return True
    else:
        return False


sum = 0
for row in range(1, len(letters)-1):
    for col in range(1, len(letters[row])-1):
        if letters[row][col] == "A":
            if cross_check(row, col):
                sum += 1

print(sum)
