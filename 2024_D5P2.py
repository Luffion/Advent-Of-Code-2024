with open("data.txt", "r") as file:
    content = file.read()
parts = content.strip().split("\n\n")
rules = [line.strip() for line in parts[0].split("\n")]
pages = [line.strip() for line in parts[1].split("\n")]
pages = list(line.strip().split(",") for line in pages)

def is_valid(page):
    valid = True
    for rule in rules:
        if rule[:2] in page and rule[-2:] in page:
            if page.index(rule[:2]) > page.index(rule[-2:]):
                valid = False
                break
    return valid

sum = 0
for page in pages:
    if is_valid(page):
        sum -= int(page[len(page)//2])
    while not is_valid(page):
        for rule in rules:
            if rule[:2] in page and rule[-2:] in page:
                page[page.index(rule[:2])] = rule[-2:]
                page[page.index(rule[-2:])] = rule[:2]
    sum += int(page[len(page)//2])

print(sum)
