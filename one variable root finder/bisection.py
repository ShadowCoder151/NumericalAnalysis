import math as m

def f(x):
    return m.asin(x) + x * m.sqrt(1 - x ** 2) - 0.5 * m.pi + 1.24

def sgn(y):
    return m.copysign(1, y)
    

def bisection(a:float, b:float, tol:float):
    if f(a) * f(b) >= 0:
        return "Root cannot be finded in that interval"
    
    m = a
    while abs(b - a) >= tol:
        m = a + (b - a) / 2
        # print(m)
        if f(m) == 0:
            return f"Root is = {m}"
        
        elif sgn(f(a)) * sgn(f(m)) < 0:
            b = m
        
        elif sgn(f(m)) * sgn(f(b)) < 0:
            a = m
    
    return f"Root is = {m:.4f}"



print(bisection(0, 1, 10**(-2)))
        
    
