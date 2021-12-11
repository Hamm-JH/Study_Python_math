import matplotlib.pyplot as plt
import numpy as np

def expr85():
    x = list(range(1, 11))
    y = []

    for i in range(10):
        y.append(3 * x[i] - 24)

    plt.plot(x, y)
    plt.grid(color='0.8')
    plt.show()

def ex87():
    x = np.arange(-1.0, 1.01, 0.01)     # x축의 값을 대입하는 명령
    y = 3 * x       # 일차함수

    plt.plot(x, y)
    plt.grid(color='0.8')
    plt.show()

from sympy import Symbol, solve

def ex91():
    a = Symbol('a')
    b = Symbol('b')
    ex1 = a + b - 1
    ex2 = 5 * a + b - 3

    print(solve((ex1, ex2)))


