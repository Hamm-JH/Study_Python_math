import matplotlib.pyplot as plt
import numpy as np

# 1차 함수 y = 2x - 24 그래프 그리기
def expr85():
    x = list(range(1, 11))
    y = []

    for i in range(10):
        y.append(3 * x[i] - 24)

    plt.plot(x, y)
    plt.grid(color='0.8')
    plt.show()

# 식을 사용하여 그래프 그리기
def ex87():
    #데이터
    # Numpy를 np라는 이름으로 임포트한다. x는 x축의 값을 대입하는 명령.
    # arange의 파라미터
    # 1 시작값 : -1.0
    # 2 종료 직전값 : 1.01
    # 3 값 간격 : 0.01
    # ★ 시작값 -1.0 ~ 종료값 1.01까지 0.01간격으로 값을 배치
    x = np.arange(-1.0, 1.01, 0.01)     # x축의 값을 대입하는 명령

    # x축 값에 대응하는 y축의 값 계산
    # 각 요소의 값에 대해 3 * x를 계산하고, 답으로 배열 y를 생성한다.
    y = 3 * x       # 일차함수

    # y =  3 * x는 Numpy를 사용하지 않을 경우 아래 파이썬 코드로 동일하게 적용 가능하다.
    # y = []
    # for i in range(len(x)):
    #     y.append(3 * x[i])

    #그래프 그리기
    plt.plot(x, y)
    plt.grid(color='0.8')
    plt.show()

# 연립방정식을 풀기 위해 sympy에서 Symbol, solve메서드 임포트
from sympy import Symbol, solve

# 연립방정식 풀기
def ex91():
    a = Symbol('a')
    b = Symbol('b')
    ex1 = a + b - 1
    ex2 = 5 * a + b - 3

    print(solve((ex1, ex2)))


import matplotlib.pyplot as plt
import numpy as np


# 직교하는 직선
def ex94():
    x = np.arange(-1, 6)    # x값
    y = 1/2 * x + 1/2       # 직선1
    y2 = -2 * x + 7         # 직선1에 직교하는 직선

    # 그래프를 그린다
    plt.plot(x, y)
    plt.plot(x, y2)
    plt.axis('equal')
    plt.grid(color = '0.8')
    plt.show()


from sympy import Symbol, solve

# 두 직선의 교점
def ex95():
    x = Symbol('x')     # 문자 정의
    y = Symbol('y')
    ex1 = -3/2*x + 6 - y    # 직선1의 식을 정의한다
    ex2 = 1/2*x + 2 - y     # 직선2의 식을 정의한다
    print(solve( (ex1, ex2) ))  # 연립방정식을 푼다. / solve안에 이중괄호 안 먹이면 '[]'이렇게 뜸