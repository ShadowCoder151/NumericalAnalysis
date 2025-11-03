import cmath as m

def f(x: complex):
    return x**4 - 3*x**3 + x**2 + x + 1


def b(p0:float, p1:float, p2: float):
    n = (p0 - p2) ** 2 * (f(p1) - f(p2)) - (p1 - p2) ** 2 * (f(p0) - f(p2))
    d = (p0 - p1) * (p1 - p2) * (p0 - p2)
    return n / d

def a(p0:float, p1:float, p2: float):
    n = (p1 - p2) * (f(p0) - f(p2)) - (p0 - p2) * (f(p1) - f(p2))
    d = (p0 - p1) * (p1 - p2) * (p0 - p2)
    return n / d

def muller(p0:float, p1:float, p2: float, tol: int):
    for i in range(1000):
        A, B, C = a(p0, p1, p2), b(p0, p1, p2), f(p2)

        D = m.sqrt(B * B - 4 * A * C)
        if abs(B + D) < abs(B - D):
            D = -D
        p3 = p2 - 2 * C / (B + D)

        if abs(p2 - p3) < (10 ** -tol):
            return f"Root is {p3:.{tol}f} in {i + 1} iterations"
    
        p0, p1, p2 = p1, p2, p3

    return "Method did not converge"


print(muller(0.5, -0.5, 0, 6))

