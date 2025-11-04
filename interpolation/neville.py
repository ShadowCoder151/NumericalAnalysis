import math as m
from typing import List

def neville(points: List[tuple], x: float):
    n = len(points)

    P = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n - 1, -1, -1):
        P[i][i] = points[i][1]
        xi = points[i][0]
        for j in range(i + 1, n):
            xj = points[j][0]

            P[i][j] = ((x - xi) * P[i + 1][j] - (x - xj) * P[i][j - 1])/(xj - xi)

    return P[0][n - 1]


points = [(x, round(m.log(x), 4)) for x in [2, 2.2, 2.3]]

x = 2.1

print(neville(points, x))
            