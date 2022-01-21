

# %matplotlib inline
# import matplotlib.pyplot as plt

import expr03
import expr04


def expr03_functions():
    # expr03.expr85()     # y = 3x - 24 그래프
    # expr03.ex87()       # 식을 사용하여 그래프 그리기(numpy)

    # .3 직선의 방정식
    # expr03.ex91()       # 두 점을 잇는 직선 / SymPy 라이브러리를 이용해 연립방정식 풀기
    # expr03.ex94()       # 직교하는 두 직선 / 점 (1, 5)를 지나며 직선 y = 1/2x + 1/2와 y = -2x - 7을 직교하는 그래프
    # expr03.ex95()       # 두 직선의 교점

    # .4 비례식과 삼각비
    # expr03.ex100()      # .2 선분을 m:n으로 내분하는 점 / 수직이등분선의 식을 구하고 그래프 그리기
    # expr03.ex105()      # .3 삼각비와 원 / 삼각비를 이용해 원 그리기
    # expr03.ex109(3, 4)  # .4 삼각비와 각도 / 직각을 사이에 둔 두 변의 비율로 각도 구하기 (밑변 4, 윗변 3)
    
    # .5 피타고라스의 정리
    # expr03.ex111(300)   # .1 원의 방정식 / 반지름이 r인 원을 방정식으로 그리기
                          # .1 원의 방정식 / 원의 중심이 원점이 아닌 다른 좌표에 있어야 할 경우
    expr03.ex113(200, 300, 300)     # (a, b, r) : 원점 x, 원점 y, 반지름 r

        # .2 두 점 사이의 거리
        # p115 이미지에서 실제 길이를 구하는 방법

    # .6 편리한 공식 p115
        # .1 점에서 직선까지의 거리 p116
        # .2 직선으로 둘러싸인 영역의 면적 p117
        # 마우스를 사용하여 원 그리기 p120

def expr04_functions():

    # .1 벡터의 연산 123
    # ..1 벡터와 화살표 123
    # ..2 벡터의 성분 124
    # ..3 벡터의 방향 126
    # expr04.ex127(2, 3)    # 127 벡터의 방향 구하기

    # ..4 벡터의 크기 128
    # ..5 벡터의 연산 129
    # expr04.ex133()  # 133 파이썬에서 벡터 연산 실행하기

    # ..6 벡터 분해 134

    # .2 벡터 방정식 136
    # expr04.ex139()  # ..1 직선을 나타내는 법 / 139 두 점을 잇는 직선의 방정식
    # expr04.ex142()  # ..2 두 직선의 교점
    # ..3 벡터를 사용하는 이유 / 143 공간도형과 벡터

    # .3 벡터의 내적 144
    expr04.ex147()    # 기여도 계산하기 / 144 철수의 기여도 구하기

    pass

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # 3장 방정식으로 도형 그리기
    # expr03_functions()

    expr04_functions()