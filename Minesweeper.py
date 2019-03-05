import random

class Minesweeper:
    def __init__(self, b, n, m):
        self.array = [['-' for x in range(m)] for x in range(n)]
        num = 0

        while num < b:
            x = random.randrange(m)
            y = random.randrange(n)

            if self.array[y][x] != '*':
                self.array[y][x] = '*'
                num += 1

    def find(self, n ,m):
        X = [-1, 0, 1, -1, 1, -1, 0, 1]
        Y = [-1, -1, -1, 0, 0, 1, 1, 1]

        for y in range(n):
            for x in range(m):
                num = 0
                if self.array[y][x] == "-":
                    for i in range(8):
                        if 0 <= x + X[i] <= m - 1 and 0 <= y + Y[i] <= n - 1:
                            if self.array[y + Y[i]][x + X[i]] == "*":
                                num += 1
                    self.array[y][x] = str(num)

        return self.array


if __name__ == '__main__':
    bomb = 20
    scale = [10, 10]
    m = Minesweeper(bomb, scale[0], scale[1])
    result = m.find(scale[0], scale[1])
    for x in result:
        print(x)

