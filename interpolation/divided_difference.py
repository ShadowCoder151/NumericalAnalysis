import math as m
from typing import List

def DD(points: List[tuple]):
    n = len(points)

    P = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        P[i][i] = points[i][1]

    for i in range(1, n):
        x, y = 0, i
        while y < n and x + 1 <= y:
            P[x][y] = (P[x + 1][y] - P[x][y - 1]) / (points[y][0] - points[x][0])
            P[x][y] = round(P[x][y], 7)
            x, y = x + 1, y + 1
    
        # for row in P:
        #     print(" ".join(f"{item:<10}" for item in row))
        
        # print("----------------")

    return P


points = [
    (1.0, 0.7651977),
    (1.3, 0.6200860),
    (1.6, 0.4554022),
    (1.9, 0.2818186),
    (2.2, 0.1103623)
]

P = DD(points)

for row in P:
    print(" ".join(f"{item:<10}" for item in row))