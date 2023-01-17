import sympy

time = [-0.2, -0.1, 0, 0.1, 0.2]  # In second
height = [1.31, 1.13, 0.89, 0.51, 0.07]  # In meter

sum_x = 0
sum_x_squared = 0
sum_x_squared_3 = 0
sum_x_squared_4 = 0
sum_xy = 0
sum_x_squared_y = 0
sum_y = 0
n = len(time)

for i, value in enumerate(height):
    sum_x_squared += time[i]**2
    sum_x_squared_3 += time[i] ** 3
    sum_x_squared_4 += time[i] ** 4
    sum_xy += time[i] * value
    sum_y += value
    sum_x_squared_y += time[i]**2 * value

a, b, c = sympy.symbols('a, b, c')
eq1 = sympy.Eq(a * n + b * sum_x + c * sum_x_squared, sum_y)
eq2 = sympy.Eq(a * sum_x + b * sum_x_squared + c * sum_x_squared_3, sum_xy)
eq3 = sympy.Eq(a * sum_x_squared + b * sum_x_squared_3 + c * sum_x_squared_4, sum_x_squared_y)
result = sympy.solve([eq1, eq2, eq3], (a, b, c))

result_a = float(result[a])
result_b = float(result[b])
result_c = float(result[c])

print(result_c * -2)
