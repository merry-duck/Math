# ОДУ вида: y" + py' + qy = 0
# Характеристическое уравнение вида: k^2 + pk + q = 0

# Зададим коэффициенты p, q
p = -4
q = 4

# Зададим начальные условия
x0 = 0  # н. у. x для y(x0) = y0
y0 = 3
x1 = 0  # н. у. x для y'(x1) = y1
y1 = -1

import sympy
import math
import cmath

eq_str = f"y'' + {p}y' + {q}y = 0"
print(eq_str)
print(f"Начальные условия: y({x0}) = {y0}, y'({x1}) = {y1}")

def discriminant_calculation(p, q):
    """Определение дискриминанта характеристического уравнения"""
    D = p ** 2 - 4 * q
    return D


D = discriminant_calculation(p, q)
print('Значение дискриминанта: D =', D)


def find_roots(p, D):
    """Определение корней характеристического уравнения """
    if D > 0:
        k1 = (- p + math.sqrt(D)) / 2
        k2 = (- p - math.sqrt(D)) / 2
    elif D == 0:
        k1 = (-p / 2)
        k2 = k1
    elif D < 0:
        k1 = (- p + cmath.sqrt(D)) / 2
        k2 = (- p - cmath.sqrt(D)) / 2
    return k1, k2


# распаковка k1, k2 из кортежа
roots = find_roots(p, D)
k1 = roots[0]
k2 = roots[1]
print('Корни характеристического уравнения:', k1, k2, sep=' ')

C1, C2, x = sympy.symbols('C1, C2, x')  # ввод перменных для символьных вычислений


def determining_the_type_of_roots(k1, k2):
    """"Функция вывода символьного решения """
    if isinstance(k1, complex) and isinstance(k2, complex):
        a = k1.real  # α
        b = abs(k1.imag)  # β в записи α + iβ
        y = sympy.exp(a * x) * (C1 * sympy.cos(b * x) + C2 * sympy.sin(b * x))
    elif not isinstance(k1, complex) and not isinstance(k2, complex) and k1 == k2:
        y = (C1 + C2 * x) * sympy.exp(k1 * x)
    elif not isinstance(k1, complex) and not isinstance(k2, complex) and k1 != k2:
        y = C1 * sympy.exp(k1 * x) + C2 * sympy.exp(k2 * x)
    return y


y = determining_the_type_of_roots(k1, k2)
print("Общее решение ОДУ: y =", y)


def find_private_solution(y, x0, y0, x1, y1):
    """Определение частного решения из начальнызх условий"""
    # Eq(a, b) равносильно равенству a = b; .subs(x, x0) → "Подставь вместо символа x конкретное число x0", → Например, если y = C1*x + C2, а x0=2, то получим C1*2 + C2
    equation1 = sympy.Eq(y.subs(x, x0), y0)  # первое уравнение для н. у
    equation2 = sympy.Eq(y.diff(x).subs(x, x1), y1)  # второе уравнение для н. у
    # print(equation1)
    # print(equation2)
    # .solve((...), (...)) - функция решения уравнений; 1 аргумент - кортеж из уравнений, 2 аргумент - кортеж переменных, которые необходимо определить
    constants = sympy.solve((equation1, equation2), (C1, C2))
    constants = {k: sympy.nsimplify(v) for k, v in constants.items()}  # преобразует десятичные дроби констант в рациональные
    print('Полученные константы интегрирования:', constants)
    y_ch = y.subs(constants)  # .solve выводит словарь, .subs замечательно принимает словарь
    return y_ch


y_ch = find_private_solution(y, x0, y0, x1, y1)
print('Частное решение ОДУ: y =', y_ch)
