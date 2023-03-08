import numpy as np
import matplotlib.pyplot as plt  # Import packages for script to run

L = 2.6  # i meter
T0n = [3.2]  # i sekund  gjennomsnitt skal bli ca 3,23 s ved 2,6 m tau
delta_T0n = 0

T0 = sum(T0n)/len(T0n)
#delta_T0 = delta_T0n / len(T0n) 
delta_T0 = ((np.sqrt(1/2) * (4*10**(-3))))/ 2  * T0
delta_L = (np.sqrt(1/2) * (4*10**(-3))) * L
max_L = 4 * L * np.sqrt(0.1 * (delta_T0/T0))
print('Max svingning = ', max_L)

g = (4*(np.pi**2) * L) / (T0**2)
delta_g = g * np.sqrt( (delta_L/L)**2 + (2*delta_T0/T0)**2 )
print('Tyngdekraften =', g, '+-', delta_g)

print(delta_g/g)