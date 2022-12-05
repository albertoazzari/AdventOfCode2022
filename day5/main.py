from copy import deepcopy


def cratemover9000(stacks9000, move):
    crates = [stacks9000[str(move[1])].pop() for _ in range(move[0])]
    stacks9000[str(move[2])].extend(crates)


def cratemover9001(stacks9001, move):
    crates = stacks9001[str(move[1])][-move[0]:]
    stacks9001[str(move[2])].extend(crates)
    del stacks9001[str(move[1])][-move[0]:]


if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    first_flag = True
    stacks9000 = {}
    stacks9001 = {}
    for i, line in enumerate(lines):
        if line == "\n" and first_flag:
            crates = [[crate[j:j + 4].strip() for j in range(0, len(crate), 4)] for crate in lines[:i - 1]]
            for j in range(len(crates[0])):
                stacks9000[str(j + 1)] = [x[j] for x in crates if not x[j] == ""]
                stacks9000[str(j + 1)].reverse()
            stacks9001 = deepcopy(stacks9000)
            first_flag = False
        elif line.startswith('move'):
            cratemover9000(stacks9000, [int(j) for j in line.split() if j.isdigit()])
            cratemover9001(stacks9001, [int(j) for j in line.split() if j.isdigit()])

    res_9000 = ""
    res_9001 = ""
    for i in stacks9000.keys():
        res_9000 += str(stacks9000[i][-1])
        res_9001 += str(stacks9001[i][-1])
    print(res_9000)
    print(res_9001)
