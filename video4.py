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
muestras = 1000 # Numero de puntos
t = np.linspace(0, 2*np.pi, muestras)

f = 8/(2*np.pi)  # 1.27 hz
señal = 8 * np.sin(2*np.pi*f*t)

# Como plotear
fig, ax = plt.subplots()
ax.plot(t, señal)
ax.set_xlabel("tiempo")
ax.set_ylabel("señal")
fig.show()

FFT = fft(señal)
frecuencias = fftfreq(len(t), t[1]-t[0])

FFT2, frec2 = fast_fourier_transform(t, señal)


# Como plotear
fig, ax = plt.subplots()
ax.stem(frecuencias, FFT)
ax.set_xlabel("Frecuencias")
ax.set_ylabel("FFT")
ax.set_xlim(-6, 6)
fig.show()


fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t, señal)
axs[0].set_xlabel('Tiempo (s)')
axs[0].set_ylabel('Amplitud')
axs[1].plot(frecuencias, FFT)
axs[1].set_xlabel('Frecuencia (Hz)')
axs[1].set_ylabel('Amplitud')
axs[1].set_xlim(0, 4)
fig.show()


fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t, señal)
axs[0].set_xlabel('Tiempo (s)')
axs[0].set_ylabel('Amplitud')
axs[1].stem(frec2, FFT2)
axs[1].set_xlabel('Frecuencia (Hz)')
axs[1].set_ylabel('Amplitud')
axs[1].set_xlim(0, 4)
fig.show()
