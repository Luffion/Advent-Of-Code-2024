with open("data.txt", "r") as file:
    map = [list(line.strip()) for line in file]

def find_arrow(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == "^":
                return i, j
    return -1, -1

row, col = find_arrow(map)
direction = "up"


at_edge = False
visited = []
while not at_edge:
    if direction == "up":
        for i in range(row, -1, -1):
            if map[i][col] != "#":
                row, col = i, col
                if (row, col) not in visited: visited.append((row, col))
            else:
                direction = "right"
                break
    elif direction == "down":
        for i in range(row, len(map[0])):
            if map[i][col] != "#":
                row, col = i, col
                if (row, col) not in visited: visited.append((row, col))
            else:
                direction = "left"
                break
    elif direction == "left":
        for i in range(col, -1, -1):
            if map[row][i] != "#":
                row, col = row, i
                if (row, col) not in visited: visited.append((row, col))
            else:
                direction = "up"
                break
    elif direction == "right":
        for i in range(col, len(map[0])):
            if map[row][i] != "#":
                row, col = row, i
                if (row, col) not in visited: visited.append((row, col))
            else:
                direction = "down"
                break
    if row == 0 and direction == "up":
        at_edge = True
    elif row == len(map)-1 and direction == "down":
        at_edge = True
    elif col == len(map)-1 and direction == "right":
        at_edge = True
    elif col == 0 and direction == "left":
        at_edge = True

print(len(visited))
