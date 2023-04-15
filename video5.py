# se importan librerias
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq

### funciones ###

def fast_fourier_transform (t, señal):
    FFT = fft(señal)
    frecuencias = fftfreq(len(t), t[1]- t[0])

    FFT = np.abs(FFT)/len(señal) # normalizar
    FFT = FFT[0:len(FFT)//2] # nos quedamos con la parte (+)
    FFT = 2*FFT # conservando la energia
    frecuencias = frecuencias[0:len(frecuencias)//2]
    return (FFT, frecuencias)

# generemos un vector temporal
muestras = 10000 # Numero de puntos
T_final = 5.5
t = np.linspace(0, T_final, muestras)

f = 3 # hz
señal = 2 * np.sin(2*np.pi*f*t)

FFT, frec = fast_fourier_transform(t, señal)

fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t, señal)
axs[0].set_xlabel('Tiempo (s)')
axs[0].set_ylabel('Amplitud')
axs[1].stem(frec, FFT)
axs[1].set_xlabel('Frecuencia (Hz)')
axs[1].set_ylabel('Amplitud')
axs[1].set_xlim(0, 10)
fig.show()


t2 = np.linspace(0, 3*T_final, 3*muestras)
señal_concatenada = np.tile(señal, 3)

fig, ax = plt.subplots()
ax.plot(t2, señal_concatenada)
fig.show()


fig, ax = plt.subplots()
ax.plot(t2, señal_concatenada)
ax.set_xlabel("tiempo")
ax.set_ylabel("señal")
ax.grid()
fig.show()


han = np.hanning(len(señal))
fig, axs = plt.subplots(2,1)
axs[0].plot(t, han, label="ventana")
axs[0].plot(t, señal, label = "señal original")
axs[1].plot(t, han*señal, label="ventana de hanning aplicada")
axs[0].legend()
axs[1].legend()
ax.set_title("ventana de hanning")
fig.show()

FFT2, frec2 = fast_fourier_transform(t, han*señal)

fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t, han*señal)
axs[0].set_xlabel('Tiempo (s)')
axs[0].set_ylabel('Amplitud')
axs[1].stem(frec2, FFT2)
axs[1].set_xlabel('Frecuencia (Hz)')
axs[1].set_ylabel('Amplitud')
axs[1].set_xlim(0, 10)
fig.show()
