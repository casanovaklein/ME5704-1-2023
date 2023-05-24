import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
from scipy import signal
plt.style.use('dark_background')

#Leer datos
Datos0=sio.loadmat('datos/estadisticos_relevantes/normal.mat')
Datos2=sio.loadmat('datos/estadisticos_relevantes/inner.mat')
Normal=Datos0['normal'].T[0]
Inner=Datos2['inner'].T[0]

#vector de tiempo
Fs=48_828 #sampling rate
dt=1/Fs #paso de tiempo
N = len(Normal)
t = np.linspace(0,dt*(N-1),N)

fig, ax = plt.subplots()
ax.plot(t, Normal, label="Sin falla")
ax.legend()
ax.set_xlabel("Tiempo [seg]")
ax.set_ylabel("Aceleracion" "$[m/s^2]$")
ax.set_title("Rodamiento sin falla")
fig.show()

fig, ax = plt.subplots()
ax.plot(t, Inner, label="Falla pista interna")
ax.legend()
ax.set_xlabel("Tiempo [seg]")
ax.set_ylabel("Aceleracion" "$[m/s^2]$")
ax.set_title("Falla pista interna")
fig.show()



#PSD
f_inner, P_xx_inner = signal.welch(x = Inner, fs = Fs, window='hann')
f_normal, P_xx_normal = signal.welch(x = Normal, fs = Fs, window='hann')

fig, ax = plt.subplots()
ax.semilogy(f_inner, P_xx_inner, label="Falla pista interna")
ax.semilogy(f_normal, P_xx_normal, label="Rodamiento sin falla")
ax.legend()
ax.set_xlabel("Frecuencia [Hz]")
ax.set_ylabel("PSD")
ax.set_title("PSD para distintos rodamientos")
fig.show()
