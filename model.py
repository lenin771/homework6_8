# Модуль для выполнения опреаций

import sympy   


def execute_expr(expr: str) -> str:         # (5+3)*10 -> 80
    """"Принимает на вход строку-пример.
    Возвращает результат примера."""
    #expr = input('Enter a task: ')
    
    try:
        ans = str(eval(expr)) 
        return ans
    except NameError:
        ans = 'Incorrect input'
        return ans
    


def solve_eq(expr: str) -> str:                    # x**3 - 8 = 0 -> "2"
                                                    # x**2 - 1 = 0 -> "1,-1"
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""

    #expr = input('Enter expr: ')
    x = sympy.Symbol('x')
    try:
        ans = sympy.solve(expr, x)
        ans = str(ans)
        return ans
    except ValueError:
        ans = 'Incorrect input'
        return ans
solve_eq(str)
def simpify_pol(expr: str) -> str:           # x**2 + 3*x**2 + 4 -> 4*x**2 + 4
    """"Упрощает введенный многочлен"""
    #expr = input('Enter expr: ')
    x = sympy.Symbol('x')
    print(expr)
    try:
        ans = sympy.simplify(expr)
        return ans
    except ValueError:
        ans = 'Incorrect input'
        return ans
    

