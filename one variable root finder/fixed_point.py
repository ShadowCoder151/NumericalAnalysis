import math as m
import random as random

def g(x):
    return 0.5 * m.sqrt(10 - x**3)
    

def fixed_point(a:float, b:float, tol:float):
    p0 = random.randint(a, b)
    for i in range(1000):
        p1 = g(p0)

        if abs(p1 - p0) < tol:
            print(f'Done in {i + 1} iterations')
            return f"root is x={p1:.9f}"
        
        p0 = p1
    
    return f"Root not found at that interval"



print(fixed_point(1, 2, 10**(-9)))
    
