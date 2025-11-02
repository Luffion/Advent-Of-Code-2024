import time

start_time = time.time()

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

def binarysearch(data, target):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
        elif data[mid] > target:
            end = mid - 1

    return -1

result = 0
for i in list1:
    s = 0
    pos = binarysearch(list2, i)
    while list2[pos] == i:
        pos -= 1
    pos += 1
    while list2[pos] == i:
        s += 1
        pos += 1
        if pos >= len(list2):
            break
    result += int(i) * s
print(result)

end_time = time.time()
elapsed_time = end_time - start_time

print(f"Execution time: {elapsed_time:.6f} seconds")
