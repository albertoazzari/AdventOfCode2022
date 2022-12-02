elf_rps = {'A': 1, 'B': 2, 'C': 3}
me_rps = {'X': 1, 'Y': 2, 'Z': 3}


def get_score_by_shape(a, b):
    if elf_rps[a] == me_rps[b]:
        return 3 + me_rps[b]
    elif (elf_rps[a] % 3) + 1 == me_rps[b]:
        return 6 + me_rps[b]
    else:
        return me_rps[b]


def get_score_by_outcome(a, b):
    if b == 'Y':
        return 3 + elf_rps[a]
    elif b == 'Z':
        return 6 + (elf_rps[a] % 3) + 1
    else:
        return 3 if elf_rps[a] == 1 else elf_rps[a]-1


if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    scores_by_shape = []
    scores_by_outcome = []
    for i in range(len(lines)):
        elf, me = lines[i].strip().split(" ")
        scores_by_shape.append(get_score_by_shape(elf, me))
        scores_by_outcome.append(get_score_by_outcome(elf, me))
    print(sum(scores_by_shape))
    print(sum(scores_by_outcome))
