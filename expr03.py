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


import matplotlib.pyplot as plt
import numpy as np

# 선분을 수직으로 이등분하는 직선
def ex100():
    # 기본이 되는 선분의 기울기와 절편
    a1 = (5-1) / (6-0)
    b1 = 1

    # 선분의 중점
    cx = (0+6) / 2
    cy = (1+5) / 2

    # 선분에 직교하는 직선의 기울기 (a2 = -1 / a1)
    a2 = -1 / a1

    # 선분에 직교하는 직선의 절편(b2 = y - a2 * x)
    b2 = cy - a2 * cx

    # 직선의 식
    x = np.arange(0, 7)     # x값
    y1 = a1 * x + b1        # 기본 직선
    y2 = a2 * x + b2        # 수직이등분선

    # 그린다
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.axis('equal')
    plt.grid(color='0.8')
    plt.show()


import matplotlib.pyplot as plt
import numpy as np

# 삼각비를 사용해 원 그리기
def ex105():
    # 각도
    th = np.arange(0, 360)

    # 원주 위에 있는 점 P의 좌표를 구하는 방법
    # sin, cos 함수를 넣으면 표의 값을 얻을 수 있으나 라디안이라고 부르는 '호도법' 단위로 지정해야 함.
    # radians() : '도수법' 단위의 각도를 호도법 단위의 각도로 바꾸는 명령어
    x = np.cos(np.radians(th))
    y = np.sin(np.radians(th))

    # 위의 x, y는 원점(0, 0)을 중심으로 원을 구하는 방법.
    # 다른 중심점 (예: (2, 3))에서 원을 그리고 싶은 경우 아래와 같이 각각 더해주면 됨
    # x = np.cos(np.radians(th)) + 2
    # y = np.sin(np.radians(th)) + 3
    
    # 다음과 같이 쓰면 반지름 r인 원도 그릴 수 있음
    # r = 5
    # x = r * np.cos(np.radians(th))
    # y = r * np.sin(np.radians(th))

    # 그리기
    plt.plot(x, y)
    plt.axis('equal')
    plt.grid(color='0.8')
    plt.show()

    # 도수법과 호도법
    # 우리들이 각도를 나타낼 때는 일반적으로 도수법을 사용하는데 컴퓨터 세계에서는 호도법을 사용한다.
    # 호도법은 원에 대한 호의 길이의 비율로 나타내는 방법이다.
    ## 반지를 r의 원주는 2πr 이므로 반지름이 1이면 원주는 2π 입니다.
    # 이때 부채율의 각도가 60도이고 호의 길이가 x라고 하면 다음과 같은 비례식이 성립합니다.
    # 360 : 2π = 60 : x
    # 이 식을 x에 관해 풀면 다음과 같은 식이 됩니다. 즉 도수법의 60도는 호도법으로는 1/3π 라디안이라는 값이 됩니다.
    # 360x = 2π Ⅹ 60
    # x = 120/360π = 1/3π


# 직각을 사이에 둔 두 변의 비율로 각도 구하기
def ex109(x, y):
    # NumPy에는 역삼각 함수도 정의돼 있다.
    # tan의 역함수는 arctan2() 함수
    # 이 함수를 사용하여 삼각형의 각도 Θ를 구한다.
    # arctan2(y, x) 밑변 x, 윗변 y
    rad = np.arctan2(x, y)  # 각도를 구한다(라디안)
    th = np.degrees(rad)    # 도수법으로 변환한다
    print(th)
    

import matplotlib.pyplot as plt
import numpy as np

# 반지름이 r인 원을 방정식으로 그리기
# r : 반지름
def ex111(r):
    # 원의 방정식
    x = np.arange(-r, r + 1)    # 반지름
    y = np.sqrt(r**2 - x**2)    # y

    # 그리기
    plt.plot(x, y)
    plt.axis('equal')
    plt.grid(color='0.8')
    plt.show()


import matplotlib.pyplot as plt
import numpy as np

# 중심이 (a, b)인 반지름이 r인 원 그리기
def ex113(a, b, r):
    # 원의 방정식
    x = np.arange(a-r, a+r+1)   # x : (a, b)를 중심으로
                                # 반지름이 300인 원을 그리는데 필요한 범위
    y = np.sqrt(r**2 - (x-a)**2) + b    # y : 원의 위쪽
    y2 = -y + 2 * b                     # y2 : 원의 아래쪽

    # 그리기
    plt.plot(x, y)
    plt.plot(x, y2)
    plt.axis('equal')
    plt.grid(color='0.8')
    plt.show()