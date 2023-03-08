import numpy as np

L = 2.4  # i meter
T0 = 3.2
T0n = [3.12, 3.18, 3.07, 3.31, 3.10, 3.12, 2.97, 3.22, 3.21, 3.15]  # sum etter 10 individuelle målinger.

mean = sum(T0n) / len(T0n)
variance = sum([((x - mean) ** 2) for x in T0n]) / len(T0n)
delta_T0n = variance ** 0.5

delta_T0 = (np.sqrt(1/2) * (4*10**(-3))) / 2 * T0
n = delta_T0n / delta_T0  # Antall målinger får å få lav usikkerhet.
print('Antall målinger: ', round(n))

max_L = 4 * L * np.sqrt(0.1 * (delta_T0/T0))
print('Max svingning = ', max_L)

T0n = []
for _ in range(20):  # Måling nr. 1
    T0n.append(63.18 / 20)
for _ in range(20):  # Måling nr. 2
    T0n.append(61.56 / 20)
for _ in range(20):  # Måling nr. 3
    T0n.append(61.56 / 20)
for _ in range(20):  # Måling nr. 4
    T0n.append(62.62 / 20)
for _ in range(20):  # Måling nr. 5
    T0n.append(61.58 / 20)
for _ in range(20):  # Måling nr. 6
    T0n.append(61.64 / 20)
for _ in range(20):  # Måling nr. 7
    T0n.append(61.98 / 20)
for _ in range(20):  # Måling nr. 8
    T0n.append(62.16 / 20)
for _ in range(20):  # Måling nr. 9
    T0n.append(62.30 / 20)
for _ in range(20):  # Måling nr. 10
    T0n.append(62.22 / 20)

accuracy = 4*10**(-3)  # Can change to 0.005

delta_T0n = 0
if abs(min(T0n) - sum(T0n)/len(T0n)) > min(T0n) - sum(T0n)/len(T0n):
    delta_T0n = abs(min(T0n) - sum(T0n)/len(T0n))
else:
    delta_T0n = abs(max(T0n) - sum(T0n)/len(T0n))

T0 = (sum(T0n)/len(T0n))
delta_T0 = (np.sqrt(1/2) * accuracy) / 2 * T0
delta_L = (np.sqrt(1/2) * accuracy) * L
print('Usikkerhet L :', delta_L, 'Usikkerhet T0n :', delta_T0n, 'Usikkerhet T0 :', delta_T0)

g = (4*(np.pi**2) * L) / (T0**2)
delta_g = g * np.sqrt((delta_L/L)**2 + (2*delta_T0/T0)**2)
print('Tyngdekraften =', g, '+-', delta_g)
print('Nøyaktighet :', delta_g/g)
