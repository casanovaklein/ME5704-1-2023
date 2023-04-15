import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
plt.style.use('dark_background')

def fast_fourier_transform (t, señal):
    FFT = fft(señal)
    frecuencias = fftfreq(len(t), t[1]- t[0])

    FFT = np.abs(FFT)/len(señal) # normalizar
    FFT = FFT[0:len(FFT)//2] # nos quedamos con la parte (+)
    FFT = 2*FFT # conservando la energia
    frecuencias = frecuencias[0:len(frecuencias)//2]
    return (FFT, frecuencias)


# Parámetros de la señal
f_continua = 10_000
fs1 = 1500  # Frecuencia de muestreo 1 (Hz)
fs2 = 120  # Frecuencia de muestreo 2 (Hz)
fs3 = 30   # Frecuencia de muestreo 3 (Hz)
fs4 = 15   # Frecuencia de muestreo 4 (Hz)
f1 = 50  # Frecuencia de la señal (Hz)

t_continua = np.linspace(0, 0.2, int(f_continua), endpoint=False)
t_fs1 = np.linspace(0, 0.2, int(fs1), endpoint=False)
t_fs2 = np.linspace(0, 0.2, int(fs2), endpoint=False)
t_fs3 = np.linspace(0, 0.2, int(fs3), endpoint=False)
t_fs4 = np.linspace(0, 0.2, int(fs4), endpoint=False)

x_continua = np.sin(2*np.pi*f1*t_continua)
x_1 = np.sin(2*np.pi*f1*t_fs1)
x_2 = np.sin(2*np.pi*f1*t_fs2)
x_3 = np.sin(2*np.pi*f1*t_fs3)
x_4 = np.sin(2*np.pi*f1*t_fs4)

fig, axs = plt.subplots(4, 1, figsize=(8, 6))
axs[0].plot(t_continua, x_continua)
axs[0].scatter(t_fs1, x_1, label = 'fs = 150',c="r", s=40)

axs[1].plot(t_continua, x_continua)
axs[1].scatter(t_fs2, x_2, label = 'fs = 120',c="r", s=40)

axs[2].plot(t_continua, x_continua)
axs[2].scatter(t_fs3, x_3, label = 'fs = 30',c="r", s=40)

axs[3].plot(t_continua, x_continua)
axs[3].scatter(t_fs4, x_4, label = 'fs = 15',c="r", s=40)

axs[0].legend()
axs[1].legend()
axs[2].legend()
axs[3].legend()

fig.show()




FFT1, frec1 = fast_fourier_transform(t_fs1, x_1)
FFT2, frec2 = fast_fourier_transform(t_fs2, x_2)
FFT3, frec3 = fast_fourier_transform(t_fs3, x_3)
FFT4, frec4 = fast_fourier_transform(t_fs4, x_4)



fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t_continua, x_continua)
axs[0].scatter(t_fs1, x_1, label = 'fs = 150',c="r", s=20)
axs[1].stem(frec1, FFT1)
axs[1].set_xlabel("Frecuencia [Hz]")
axs[0].set_title("Frecuencia de muestreo 150")
axs[1].set_xlim(0, 200)
fig.show()


fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t_continua, x_continua)
axs[0].scatter(t_fs2, x_2, label = 'fs = 120',c="r", s=20)
axs[1].stem(frec2, FFT2)
axs[1].set_xlabel("Frecuencia [Hz]")
axs[0].set_title("Frecuencia de muestreo 120")
axs[1].set_xlim(0, 200)
fig.show()

fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t_continua, x_continua)
axs[0].scatter(t_fs3, x_3, label = 'fs = 30',c="r", s=20)
axs[1].stem(frec3, FFT3)
axs[1].set_xlabel("Frecuencia [Hz]")
axs[0].set_title("Frecuencia de muestreo 30")
axs[1].set_xlim(0, 200)
fig.show()

fig, axs = plt.subplots(2, 1, figsize=(8, 6))
axs[0].plot(t_continua, x_continua)
axs[0].scatter(t_fs4, x_4, label = 'fs = 15',c="r", s=20)
axs[1].stem(frec4, FFT4)
axs[1].set_xlabel("Frecuencia [Hz]")
axs[0].set_title("Frecuencia de muestreo 15")
axs[1].set_xlim(0, 200)
fig.show()
