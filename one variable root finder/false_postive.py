import math as m

def f(x):
    return m.cos(x) - x

def false_positive(a:float, b:float, tol:float):
    if f(a) * f(b) >= 0:
        return "Method fails because sign change fails"

    for i in range(1000):
        if(f(b) - f(a)) == 0:
            return "Method fails, division by zero"
        
        c = (a * f(b) - b*f(a))/(f(b) - f(a))

        if abs(f(c)) < tol or abs(b - a) < tol:
            print(f"Done at {i + 1} iterations")
            return f"Root = {c}"
        
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
    
    return "Method fails because it did not converge."


print(false_positive(0, m.pi/4, 10 ** -9))