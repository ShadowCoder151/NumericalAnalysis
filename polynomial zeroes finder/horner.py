import math as m
from typing import List

def horner(P: List[int], root: int):
    l = len(P)
    
    Q = []
    Q.append(P[0])

    for i in range(1, l):
        Q.append(P[i] + Q[-1] * root)

    return f"{[root]}{Q[:-1]}{Q[-1:]}"

P = [2, 0, -3, 3, -4]
root = -2
print(horner(P, root))

