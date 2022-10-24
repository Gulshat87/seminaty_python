import sympy
from sympy.solve import solve
from sympy import Symbol

def evaluate_expr(expr):
    x = sympy.Symbol('x')
    return str(sympy.solve(expr,x))
