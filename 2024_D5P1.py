with open("data.txt", "r") as file:
    content = file.read()
parts = content.strip().split("\n\n")
rules = [line.strip() for line in parts[0].split("\n")]
pages = [line.strip() for line in parts[1].split("\n")]
pages = list(line.strip().split(",") for line in pages)

sum = 0
for page in pages:
    valid = True
    for rule in rules:
        if rule[:2] in page and rule[-2:] in page:
            if page.index(rule[:2]) > page.index(rule[-2:]):
                valid = False
                break
    if valid: sum += int(page[len(page)//2])
print(sum)
