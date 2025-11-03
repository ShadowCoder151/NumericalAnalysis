import sympy as sp
import math as m
import random

x = sp.symbols('x')

class f:
    def __init__(self, func: str):
        self.F = sp.sympify(func)
        self.D = sp.diff(self.F, x)

        self._f = sp.lambdify(x, self.F, 'numpy')
        self._d = sp.lambdify(x, self.D, 'numpy')

    def val(self, p:float):
        return self._f(p)
    
    def d_val(self, p:float):
        return self._d(p)
    

def new_rap(func:str, a:float, b:float, tol:float):
    g = f(func)

    if g.D is None:
        return "Retry with a different function"

    x0 = random.randint(a, b)

    for i in range(1000):
        
        x1 = x0 - g.val(x0)/g.d_val(x0)
        if abs(x0 - x1) < tol:
            print(f'Done in {i + 1} iterations')
            return f"Root is x = {x1}"
        
        x0 = x1
    
    return "Root not found at that interval"


func = "cos(x)-x"
print(new_rap(func, 0, 1, 10**(-6)))