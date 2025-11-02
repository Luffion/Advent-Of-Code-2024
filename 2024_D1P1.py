with open("data.txt", "r") as file:
    lines = [line.strip().split() for line in file]

list1 = [line[0] for line in lines]
list2 = [line[1] for line in lines]

def quicksort(data, start, end):
    if start >= end:
        return

    pivot = data[start]
    i = start - 1
    j = end + 1

    while True:
        while True:
            i += 1
            if data[i] >= pivot:
                break

        while True:
            j -= 1
            if data[j] <= pivot:
                break

        if i >= j:
            break

        data[i], data[j] = data[j], data[i]

    quicksort(data, start, j)
    quicksort(data, j + 1, end)

    return data

list1 = quicksort(list1, 0, len(list1) - 1)
list2 = quicksort(list2, 0, len(list2) - 1)

s = 0
for i in range(len(list1)):
    s += abs(int(list1[i]) - int(list2[i]))
print(s)
