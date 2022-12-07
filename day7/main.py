from collections import defaultdict

if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    path = []
    file_system = defaultdict(lambda: 0)
    for line in lines:
        commands = line.strip().split()
        if commands[1] == "cd":
            if not commands[2] == "..":
                path.append(commands[2])
            else:
                path.pop()
        elif commands[0].isdigit():
            dim = int(commands[0])
            for i in range(1, len(path) + 1):
                file_system['/'.join(path[:i])] += dim

    tot_size = sum([v for _, v in file_system.items() if v <= 100000])
    print(tot_size)

    free_space = file_system['/'] - (70000000 - 30000000)
    min_folder_size = min([v for _, v in file_system.items() if v >= free_space])
    print(min_folder_size)