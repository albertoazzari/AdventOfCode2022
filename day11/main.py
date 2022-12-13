monkeys = []

for group in open("input.txt").read().strip().split("\n\n"):
    lines = group.splitlines()
    monkey = []
    monkey.append(eval(lines[1].split(": ")[1]))
    monkey.append(eval("lambda old:" + lines[2].split("=")[1]))
    for line in lines[3:]:
        monkey.append(int(line.split()[-1]))
    monkey.append(0)
    monkeys.append(monkey)

# monkey [0] item
# monkey [1] function
# monkey [2] test
# monkey [3] test == true
# monkey [4] test == false
# monkey [5] items inspected

# module trick
mod = 1
for monkey in monkeys:
    mod *= monkey[2]


for _ in range(20): # change to 10000 for part 2
    for monkey in monkeys:
        if monkey[0]:
            for item in monkey[0]:
                item = monkey[1](item) // 3# remove //3 for part 2
                item %= mod
                if item%monkey[2] == 0:
                    if isinstance(monkeys[monkey[3]][0], int):
                        monkeys[monkey[3]][0] = (monkeys[monkey[3]][0], item)
                    else:
                        monkeys[monkey[3]][0] += (item,)
                else:
                    if isinstance(monkeys[monkey[4]][0], int):
                        monkeys[monkey[4]][0] = (monkeys[monkey[4]][0], item)
                    else:
                        monkeys[monkey[4]][0] += (item,)
            monkey[5] += len(monkey[0])
            monkey[0] = []
mb = [x[5] for x in monkeys]
mb.sort(reverse=True)
business_count = mb[0]*mb[1]
print(f"{business_count = }")
