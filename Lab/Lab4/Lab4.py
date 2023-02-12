import math
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 5, 3, 8, 7]

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
to_B = B * 2
# print('A:', A, '   B:', B, '     lambda:', to_B)

for i in range(len(x)):
    sigma_y += math.sqrt((1 / (N - 2)) * (y[i] - A - B * x[i]) ** 2)

sigma_A = sigma_y * math.sqrt(x_kvadrat_sum / delta)
sigma_B = sigma_y * math.sqrt(N / delta)

print('A:', A, '  B: ', B, '     usikkerthet til A:', sigma_A, 'usikkerheten til y:', sigma_y,
      'sigma b:', sigma_B)

list_plot_y = []
for i in range(len(x)):
    y_1 = A + B*x[i]
    list_plot_y.append(y_1)

plt.scatter(x, y, color='blue')
plt.plot(x, list_plot_y, color='green')
plt.show()
