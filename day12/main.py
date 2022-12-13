from collections import deque


def get_pos(grid: [[int]]) -> ([(int, int, int)], (int, int)):
    start = []
    end = []
    row = len(grid)
    col = len(grid[0])
    for i in range(row):
        for j in range(col):
            if grid[i][j] == ord("S"):
                start.append((grid[i][j], i, j))
                grid[i][j] = ord('a')
            elif grid[i][j] == ord("a"):
                start.append((grid[i][j], i, j))
            elif grid[i][j] == ord("E"):
                end = (i, j)
                grid[i][j] = ord('z')
    return start, end

def dfs(start_point, end_point):
    q = deque()
    q.append((0, start_point[0], start_point[1]))
    visited = set()
    visited.add(start_point)
    while q:
        step, row, col = q.popleft()
        for i, j in [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]:
            # out of the grid case
            if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0])-1:
                continue
            # already visited case
            if (i, j) in visited:
                continue
            # difference higher than 1 case
            if grid[i][j] > grid[row][col] + 1:
                continue
            #endpoint reach case
            if i == end_point[0] and j == end_point[1]:
                return step+1
            # if cell is valid, inside the grid, new and not the end point: do bfs
            node = (step+1, i, j)
            visited.add((i, j))
            q.append(node)

if __name__ == "__main__":
    grid = [[ord(x) for x in line.strip()] for line in open("input.txt").readlines()]
    sp, ep = get_pos(grid)
    min_steps = len(grid)*len(grid[0])
    for point in sp:
        start = (point[1], point[2])
        steps = dfs(start, ep)
        if chr(point[0]) == "S":
            print(f"Part 1:\n {steps = }")
        min_steps = min(min_steps, steps if not steps is None else len(grid) * len(grid[0]))
    print(f"Part 2:\n {min_steps = }")






