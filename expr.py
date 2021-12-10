import matplotlib.pyplot as plt

def expr85():
    x = list(range(1, 11))
    y = []

    for i in range(10):
        y.append(3 * x[i] - 24)

    plt.plot(x, y)
    plt.grid(color='0.8')
    plt.show()

def inExpr():
    y = []
    for x in range(1, 11):
        y.append(3 * x -24)

    print(y)


