with open("data.txt", "r") as f:
    letters = [list(line.strip()) for line in f]

step = 4

def directional_check(row, col, dr, dc):
    return ''.join(letters[row + i * dr][col + i * dc] for i in range(step))

sum = 0
for row in range(len(letters)):
    for col in range(len(letters[row])):
        if letters[row][col] == "X":
            if row <= len(letters) - step:
                if directional_check(row, col, 1, 0) == "XMAS": sum += 1 #RIGHT
            if row >= step-1:
                if directional_check(row, col, -1, 0) == "XMAS": sum += 1  #LEFT
            if col <= len(letters[row]) - step:
                if directional_check(row, col, 0, 1) == "XMAS": sum += 1 #DOWN
            if col >= step-1:
                if directional_check(row, col, 0, -1) == "XMAS": sum += 1 #UP
            if row <= len(letters) - step and col <= len(letters[row]) - step:
                if directional_check(row, col, 1, 1) == "XMAS": sum += 1 #DOWN-RIGHT
            if row <= len(letters) - step and col >= step-1:
                if directional_check(row, col, 1, -1) == "XMAS": sum += 1 #DOWN-LEFT
            if row >= step-1 and col <= len(letters[row]) - step:
                if directional_check(row, col, -1, 1) == "XMAS": sum += 1 #UP-RIGHT
            if row >= step-1 and col >= step-1:
                if directional_check(row, col, -1, -1) == "XMAS": sum += 1 #UP-LEFT
print(sum)
