x = 1

signal_strength = []
lines = open("input.txt").readlines()
for line in lines:
    if line == "noop\n":
        signal_strength.append(x)
    else:
        v = int(line.split()[1])
        signal_strength.append(x)
        signal_strength.append(x)
        x += v

print(sum(x * y + y for x, y in list(enumerate(signal_strength))[19::40]))

for i in range(0, len(signal_strength), 40):
    for j in range(40):
        print(end="##" if abs(signal_strength[i + j] - j) <= 1 else "  ")
    print()