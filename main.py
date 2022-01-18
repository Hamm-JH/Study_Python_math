

# %matplotlib inline
# import matplotlib.pyplot as plt

import expr03


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
    # (a, b, r) : 원점 x, 원점 y, 반지름 r
    expr03.ex113(200, 300, 300)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    expr03_functions()