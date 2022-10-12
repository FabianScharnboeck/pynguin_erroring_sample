from matplotlib import pyplot as plt


def create_plot():
    listx: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    listy: list = [3, 6, 8, 1, 30, 40, 50, 80, 30]
    plt.plot(listx, listy)
    plt.savefig("./my_fig.jpg")

