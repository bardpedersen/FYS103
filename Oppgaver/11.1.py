import numpy as np
import matplotlib.pyplot as plt

my = 0.5
list_of_nu = [0, 1, 2, 3, 4, 5, 6]


def poisson(my_1, nu):
    ans = np.e**(-my_1)*((my_1**nu)/np.math.factorial(nu))
    return ans


list_to_histogram = []
for number, i in enumerate(list_of_nu):
    list_to_histogram.append(poisson(my, i))

bins = list_of_nu
plt.bar(bins, list_to_histogram, linewidth=1)
plt.legend(['List of nu values'])
plt.show()
