import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

def animate(frame):
    global ax
    x = [1, 2, 3, 4]
    y = [2, 4, 6, 8]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.plot(x[:frame], y[:frame])



def run():
    global fig
    simple_animation = animation.FuncAnimation( fig,
                                               animate,
                                               frames = 10,
                                               interval = 1000)
    plt.show()
run()