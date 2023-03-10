import numpy as np

L = 2.4  # Length of rope in m
T0 = 3.2  # Time from lab manual to calculate number of fluctuations
T0n = [3.12, 3.18, 3.07, 3.31, 3.10, 3.12, 2.97, 3.22, 3.21, 3.15]  # Time of 10 measurements
# to calculate standard error

# Calculate standard error for time measurement
mean = sum(T0n) / len(T0n)
variance = sum([((x - mean) ** 2) for x in T0n]) / len(T0n)
delta_T0n = variance ** 0.5

delta_T0 = (np.sqrt(1 / 2) * (4 * 10 ** (-3))) / 2 * T0

n = delta_T0n / delta_T0  # Number of measurements to get low uncertainty.
print('Antall målinger: ', round(n))

max_L = 4 * L * np.sqrt(0.1 * (delta_T0 / T0))  # The maximum pendulum swing to get low uncertainty.
print('Max svingning = ', max_L)

# Since n = 19, the number of swings in one time measurement is 20.
T0n = []
for _ in range(20):  # Measurement nr. 1
    T0n.append(63.18 / 20)
for _ in range(20):  # Measurement nr. 2
    T0n.append(61.56 / 20)
for _ in range(20):  # Measurement nr. 3
    T0n.append(61.56 / 20)
for _ in range(20):  # Measurement nr. 4
    T0n.append(62.62 / 20)
for _ in range(20):  # Measurement nr. 5
    T0n.append(61.58 / 20)
for _ in range(20):  # Measurement nr. 6
    T0n.append(61.64 / 20)
for _ in range(20):  # Measurement nr. 7
    T0n.append(61.98 / 20)
for _ in range(20):  # Measurement nr. 8
    T0n.append(62.16 / 20)
for _ in range(20):  # Measurement nr. 9
    T0n.append(62.30 / 20)
for _ in range(20):  # Measurement nr. 10
    T0n.append(62.22 / 20)

accuracy = 4 * 10 ** (-3)  # The manual wanted a certainty closer than 0.05% so this
# accuracy is set to 0.04%

# Formulas are retrieved from the lab manual. Here the uncertainty is calculated.
T0 = (sum(T0n) / len(T0n))
delta_T0 = (np.sqrt(1 / 2) * accuracy) / 2 * T0
delta_L = (np.sqrt(1 / 2) * accuracy) * L
print('Usikkerhet L :', delta_L, 'Usikkerhet T0n :', delta_T0n, 'Usikkerhet T0 :', delta_T0)

# Formulas are retrieved from the lab manual. Here the gravity and its uncertainty is calculated.
g = (4 * (np.pi ** 2) * L) / (T0 ** 2)
delta_g = g * np.sqrt((delta_L / L) ** 2 + (2 * delta_T0 / T0) ** 2)
print('Tyngdekraften =', g, '+-', delta_g)
print('Nøyaktighet :', delta_g / g)
