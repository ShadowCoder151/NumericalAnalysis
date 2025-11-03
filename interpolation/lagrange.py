import math as m
from typing import List


def product(P:List[tuple], x:float):
    prod = 1
    for xi, _ in P:
        prod *= (x - xi)
    return prod

def d_prod(P:List[tuple], k:int):
    prod = 1
    xk = P[k][0]
    for i, pi in enumerate(P):
        xi, _ = pi
        if i != k:
            prod *= (xk - xi)
    return prod



def lagrange(P:List[tuple], x:float):
    S = 0
    Nn = product(P, x)

    for k, pk in enumerate(P):
        xk, yk = pk
        Nk = Nn / (x - xk)
        Dk = d_prod(P, k)

        Lk = Nk / Dk

        S = S + yk * Lk
    
    return S


P = [(2, 1/2), (2.75, 1/2.75), (4, 1/4)]
x = 3

print(lagrange(P, x))
       
