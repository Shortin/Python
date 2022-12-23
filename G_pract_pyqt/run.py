import psutil
from datetime import datetime as dt
from collections import deque
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def func():
    N=600
    x = deque([dt.now()], maxlen=N)
    y = deque([0], maxlen=N)

    fig, ax = plt.subplots()
    line, = ax.plot_date(x, y, '-')



    def animate(i):
        x.append(dt.now())
        y.append(psutil.cpu_percent(1))
        ax.autoscale_view(True)
        line.set_data(x, y)
        ax.fill_between(x, y, color='white')
        return line,


    ani = animation.FuncAnimation(fig, animate)
    plt.show()

func()