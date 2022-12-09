
def move(H, T):
    dist_x = abs(H[0] - T[0])
    dist_y = abs(H[1] - T[1])
    if dist_x <= 1 and dist_y <= 1:
        pass
    elif dist_x >= 2 and dist_y >= 2:
        T = (H[0] - 1 if T[0] < H[0] else H[0] + 1, H[1] - 1 if T[1] < H[1] else H[1] + 1)
    elif dist_x >= 2:
        T = (H[0] - 1 if T[0] < H[0] else H[0] + 1, H[1])
    elif dist_y >= 2:
        T = (H[0], H[1] - 1 if T[1] < H[1] else H[1] + 1)
    return T


def part1():
    H, T = ((0, 0) for i in range(2))
    positions = set()
    positions.add(T)
    for line in open('input.txt', 'r').readlines():
        dir, step = line.strip().split()
        step = int(step)
        for _ in range(step):
            if dir == "U":
                H = (H[0], H[1] + 1)
            elif dir == "D":
                H = (H[0], H[1] - 1)
            elif dir == "R":
                H = (H[0] + 1, H[1])
            elif dir == "L":
                H = (H[0] - 1, H[1])
            T = move(H, T)
            positions.add(T)
    print(len(positions))


def part2():
    H = (0, 0)
    T = [(0, 0) for i in range(9)]
    positions = set()
    positions.add(T[-1])
    for line in open('input.txt', 'r').readlines():
        dir, step = line.strip().split()
        step = int(step)
        for _ in range(step):
            if dir == "U":
                H = (H[0], H[1] + 1)
            elif dir == "D":
                H = (H[0], H[1] - 1)
            elif dir == "R":
                H = (H[0] + 1, H[1])
            elif dir == "L":
                H = (H[0] - 1, H[1])
            T[0] = move(H, T[0])
            for i in range(1, 9):
                T[i] = move(T[i - 1], T[i])
            positions.add(T[-1])
    print(len(positions))


if __name__ == "__main__":
    part1()
    part2()




