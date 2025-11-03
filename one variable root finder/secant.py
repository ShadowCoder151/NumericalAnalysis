import math as m

def f(x):
    return m.cos(x) - x

def secant(x0:float, x1:float, tol:float):
    for i in range(1000):
        if(f(x1) - f(x0)) == 0:
            return "Method fails"
        
        x2 = (x0 * f(x1) - x1*f(x0))/(f(x1) - f(x0))

        x0, x1 = x1, x2
        if abs(x0 - x1) < tol:
            print(f"Done at {i + 1} iterations")
            return f"Root = {x1}"
    
    return "Method fails because it did not converge."


print(secant(0, m.pi/4, 10 ** -9))