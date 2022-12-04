
def fully_containing(start_elf1, end_elf1, start_elf2, end_elf2):
    if int(start_elf1) >= int(start_elf2) and int(end_elf1) <= int(end_elf2):
        return True
    elif int(start_elf2) >= int(start_elf1) and int(end_elf2) <= int(end_elf1):
        return True
    else:
        return False


def overlapping(start_elf1, end_elf1, start_elf2, end_elf2):
    xs = set(range(int(start_elf1), int(end_elf1)+1, 1))
    return len(xs.intersection(range(int(start_elf2), int(end_elf2)+1, 1))) > 0


if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    fully_contained = []
    overlap = []
    for i in range(len(lines)):
        elf1, elf2 = lines[i].strip().split(',')
        start_elf1, end_elf1 = elf1.split('-')
        start_elf2, end_elf2 = elf2.split('-')
        fully_contained.append(fully_containing(start_elf1, end_elf1, start_elf2, end_elf2))
        overlap.append(overlapping(start_elf1, end_elf1, start_elf2, end_elf2))
    print(sum(fully_contained))
    print(sum(overlap))