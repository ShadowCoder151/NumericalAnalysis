import math as m
import random as random

def g(x):
    return 0.5 * m.sqrt(10 - x**3)
    

def steffenson(a:float, b:float, tol:float):
    p0 = random.randint(a, b)
    for i in range(1000):
        p1 = p0 - (g(p0) - p0) ** 2 / (p0 + g(g(p0)) - 2*g(p0))

        if abs(p1 - p0) < tol:
            print(f'Done in {i + 1} iterations')
            return f"root is x={p1:.9f}"
        
        p0 = p1

    return f"Root not found at that interval"



print(steffenson(1, 2, 10**(-9)))
    
