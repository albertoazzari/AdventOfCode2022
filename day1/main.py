import numpy as np

if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    cal = []
    elf = []
    for i in range(len(lines)):
        if lines[i] == '\n':
            cal.append(elf)
            elf = []
        else:
            elf.append(int(lines[i].strip()))
    cal = [sum(x) for x in cal]
    cal.sort(reverse=True)
    print(f"First problem: {cal[0]}")
    print(f"Second problem: {sum(cal[:3])}")