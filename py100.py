# -*- coding: UTF-8 -*-
# python 练习100道题

import cmath


def helloWorld():
    '''
    001
    打印输出 'Hello World!'
    '''
    print('Hello World!')


def sum():
    """
    002
    根据输入的数字进行求和
    """
    firstNumber = float(input("请输入第一个数字："))
    secendNumber = float(input("请输入第二个数字："))
    sum = firstNumber + secendNumber
    print('数字{0} 和数字{1}的和是：{2}'.format(firstNumber, secendNumber, sum))


def sum2():
    '''
    003
    输入一组数字，计算数字的和，要求每个数字之间用空格隔开
    '''

    sum = 0
    inputNum = input("请输入一组数字（数字之间用空格相隔）：")
    num = inputNum.split(' ')
    for i in num:
        sum += float(i)
    print(sum)


def sqrt():
    """
    004
    对输入的正数进行开平方根
    """
    inputNum = float(input("请输入数字："))
    sqrt = inputNum ** 0.5
    print(sqrt)


def quadratic():
    """
    005
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
    006
    计算三角形的面积
    已知三角形三边长
    """
    a = float(input('输入第一条边长a:'))
    b = float(input('输入第一条边长b:'))
    c = float(input('输入第一条边长c:'))
    if a + b > c and a + c > b and b + c > a: 
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c))**0.5
        print('三角形的面积是%0.2f'%s)
    else:
        print('输入三条边构不成三角形')


def circleArea():
    """
    007
    计算圆的面积
    已知圆的半径
    """
    p = 3.14
    r = float(input('请输入圆的半径：'))
    s = p * r * r
    print('半径为{0}圆的面积是{1}'.format(r, s))







if __name__ == '__main__':

    # helloWorld()
    # sum()
    # sum2()
    # sqrt()
    # quadratic()
    # triangleArea()
    circleArea()