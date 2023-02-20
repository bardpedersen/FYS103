import math
import matplotlib.pyplot as plt  # Import packages for script to run

y = [1.845, 1.416, 1.286, 0.708, 0.580]  # Data that will be the y-values in Volt
list_of_nm = [365, 405, 436, 546, 577]  # Data that will be the x-values in nm
speed_of_light = 299792458  # The speed of light in m/s
x = []
for i in range(len(list_of_nm)):
    temp = speed_of_light / (list_of_nm[i] * (10 ** (-9)))  # Turn wavelength to frequency in Hz
    x.append(temp)

"""
Create variables and calculate A and B.
"""
x_sum = 0
x_kvadrat_sum = 0
y_sum = 0
xy_sum = 0
N = len(x)
sigma_y = 0
for i in range(len(x)):
    x_sum += x[i]
    xy_sum += x[i] * y[i]
    y_sum += y[i]
    x_kvadrat_sum += x[i] ** 2

delta = N * x_kvadrat_sum - x_sum ** 2
A = (y_sum * x_kvadrat_sum - x_sum * xy_sum) / delta
B = (N * xy_sum - x_sum * y_sum) / delta

"""
Calculate all the standard error.
"""
for i in range(len(x)):
    sigma_y += math.sqrt((1 / (N - 2)) * (y[i] - A - B * x[i]) ** 2)

sigma_A = sigma_y * math.sqrt(x_kvadrat_sum / delta)
sigma_B = sigma_y * math.sqrt(N / delta)

print('A:', A, '  B: ', B, '\n', 'Standard error to A:', sigma_A,
      'Standard error to b:', sigma_B, 'Standard error to y:', sigma_y)

"""
Calculate Placks constant.
"""

e = 1.60217656535 * (10 ** (-19))  # elementary charge in Colomb
h = 6.62607015 * (10**-34)  # The true value of Placks constant

print('Placks constant: ', B*e, 'Standard error to Placks constant: ', sigma_B * e)
print('Accuracy in percentage', (100 - ((B*e)/h) * 100))


"""
For plotting the line and data.
"""
list_plot_y = []
for i in range(len(x)):
    y_1 = A + B*x[i]
    list_plot_y.append(y_1)

plt.scatter(x, y, color='blue')
plt.plot(x, list_plot_y, color='green')

B = h/e
list_plot_y = []
for i in range(len(x)):
    y_1 = A + B*x[i]
    list_plot_y.append(y_1)

plt.plot(x, list_plot_y, color='red')
plt.title('Fotoelektrisk effekt', fontsize=18)
plt.xlabel('Frekvens oppgitt i Hz', fontsize=16)
plt.ylabel('Volt oppgitt i V', fontsize=16)
plt.legend(['Rådata', 'Regresjonsline', 'Regresjonsline med Plancks konstant'], fontsize=12)
plt.savefig('lab4.png')
