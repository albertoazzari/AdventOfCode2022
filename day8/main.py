import numpy as np

if __name__ == "__main__":
    file = open('input.txt', 'r')
    lines = file.readlines()
    count = 0
    matrix = np.array([[int(x) for x in line.strip()] for line in lines])
    rows, columns = matrix.shape
    for row in range(rows):
        for col in range(columns):
            k = matrix[row, col]
            count += all(k > matrix[row, :col]) or all(k > matrix[row, col + 1:]) or all(
                k > matrix[:row, col]) or all(k > matrix[row + 1:, col])
    print(count)

    max_score = 0
    for row in range(rows):
        for col in range(columns):
            k = matrix[row, col]
            r = k > matrix[row, col + 1:]
            l = k > np.flip(matrix[row, :col])
            t = k > np.flip(matrix[:row, col])
            d = k > matrix[row + 1:, col]
            count = 1
            for v in [r, l, t, d]:
                if v.size == 0:
                    continue
                temp = np.argwhere(v == False).flatten()
                if not len(temp) == 0:
                    count *= (temp[0] + 1)
                else:
                    count *= len(v)
            max_score = max(count, max_score)
    print(max_score)
