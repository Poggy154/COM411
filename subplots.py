import matplotlib.pyplot as plt

def read_data(file_path):
    temps = []
<<<<<<< HEAD

    with open(file_path) as file:
        for line in file:
            temps.append(float(line.strip()))

    return temps

def run():
    data = read_data("temps.txt")
    fig, axs = plt.subplots(1, 2, sharey="row")

    days = range(1, 8)

    axs[0].plot(days, data)
    axs[1].plot(days. data)

    axs[0].set_xlim(min(days), max(days))
    axs[1].set_xlim(min(days), max(days))

    axs[0].set_xlabel("Day")
    axs[0].set_ylabel("Temperature")
    axs[1].set_xlabel("Day")

    plt.tight_layout()
    plt.show()

run()
=======
    with open(file_path) as file:
        for line in file:
            temps.append(float(line.strip()))
    return temps

def run():
    data = read_data('temps.txt')
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot(range(len(data)), data)
    ax2.bar(range(len(data)), data)
    plt.show()

run()
>>>>>>> 1c2fe6c4a88bde90e773b61831b9e3878ad21e54
