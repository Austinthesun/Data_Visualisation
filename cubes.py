import matplotlib.pyplot as plt

def cubes_of_numbers(numbers):

    x_values = range(1, numbers + 1)
    y_values = [x**3 for x in x_values]

    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(x_values, y_values, c='red', linewidth=3)

    ax.set_title("Cubes", fontsize=24)
    ax.set_xlabel("Value", fontsize=14)
    ax.set_ylabel("Cubes of Value", fontsize=14)


    ax.tick_params(axis='both', which='major', labelsize=14)
    plt.show()

#cubes_of_numbers(5)
cubes_of_numbers(5000)