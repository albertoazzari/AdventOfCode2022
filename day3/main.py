
if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    dup_items = []
    for i in range(len(lines)):
        items = lines[i].strip()
        n = len(items)
        intersect = set(items[0:n // 2]).intersection(set(items[n // 2:]))
        for dup in intersect:
            dup_items.append(ord(dup)-ord('a')+1 if dup.islower() else ord(dup)-ord('A')+27)
    print(sum(dup_items))
    dup_items = []
    for i in range(0, len(lines), 3):
        items = [set(lines[i+j].strip()) for j in range(3)]
        n = len(items)
        intersect = set.intersection(*items)
        for dup in intersect:
            dup_items.append(ord(dup)-ord('a')+1 if dup.islower() else ord(dup)-ord('A')+27)
    print(sum(dup_items))


