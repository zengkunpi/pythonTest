# python菜鸟教程100题

import cmath


def quadratic():
    """
    004
    二次方程式 ax**2 + bx + c = 0
    a、b、c 用户提供,为实数,a ≠ 0           
    """
    a = float(input('输入a:'))
    b = float(input('输入b:'))
    c = float(input('输入c:'))

    d = (b**2) - (4*a*c)

    sol1 = (-b - cmath.sqrt(d))/(2*a)
    sol2 = (-b + cmath.sqrt(d))/(2*a)

    print('二次方程的解是{0}和{1}'.format(sol1, sol2))


def triangleArea():
    """
    005
    计算三角形的面积
    已知三角形三边长
    """
    a = float(input('输入第一条边长a:'))
    b = float(input('输入第一条边长b:'))
    c = float(input('输入第一条边长c:'))

    p = (a + b + c) / 2

    s = (p * (p - a) * (p - b) * (p - c))**0.5

    print('三角形的面积是%0.2f'%s)


def circleArea():
    """
    006
    计算圆的面积
    已知圆的半径
    """
    p = 3.14
    r = float(input('请输入圆的半径：'))
    s = p * r * r
    print('半径为{0}圆的面积是{1}'.format(r, s))

    









# quadratic()
# triangleArea()
circleArea()