#importar librerías
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert, chirp
from scipy.fftpack import fft, fftfreq
from mpl_toolkits.mplot3d import Axes3D

def fast_fourier_transform (t, señal):
    FFT = fft(señal)
    frecuencias = fftfreq(len(t), t[1]- t[0])

    FFT = np.abs(FFT)/len(señal) # normalizar
    FFT = FFT[0:len(FFT)//2] # nos quedamos con la parte (+)
    FFT = 2*FFT # conservando la energia
    frecuencias = frecuencias[0:len(frecuencias)//2]
    return (FFT, frecuencias)

#leer datos
Datos0=sio.loadmat('datos/Hilbert/inner.mat')
x=Datos0['x'][:, 0]
t=np.transpose(Datos0['t'])[:, 0]

#graficar
fig, ax = plt.subplots()
ax.plot(t,x,linewidth=1)
ax.set_xlabel('Tiempo (s)', fontsize=14)
ax.set_ylabel('Aceleración ' "$(m/s^2)$", fontsize=14)
ax.set_ylim(-4,4)
fig.show()


#calcular envolvente
env= np.abs(hilbert(x))
# graficamos la señal analitica
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
parte_real = hilbert(x).real
parte_img = hilbert(x).imag
ax.plot(t[0:1000], parte_img[0:1000], parte_real[0:1000])
ax.set_xlim(0, 0.05)
ax.set_xlabel('Tiempo')
ax.set_ylabel('Parte imaginaria')
ax.set_zlabel('Parte real')
fig.show()



#graficar
fig, ax = plt.subplots()
ax.plot(t,x,linewidth=1)
ax.plot(t,env,linewidth=1)
ax.set_xlabel('Tiempo (s)', fontsize=14)
ax.set_ylabel('Aceleración ' "$(m/s^2)$", fontsize=14)
ax.set_xlim(0,0.05)
ax.set_ylim(-4,4)
fig.show()


#Transformada de Fourier
fft_sin_env, frec_sin_env = fast_fourier_transform(t, x)
fft_con_env, frec_con_env = fast_fourier_transform(t, env)



fig, ax = plt.subplots()
ax.plot(frec_sin_env, fft_sin_env)
ax.set_xlabel('Frecuencia (Hz)', fontsize=14)
ax.set_ylabel('Aceleración ' "$(m/s^2)$", fontsize=14)
ax.set_title('Sin envolvente')
ax.set_xlim(0,200)
ax.set_ylim(0,0.4)
fig.show()



fig, ax = plt.subplots()
ax.plot(frec_con_env, fft_con_env)
ax.set_xlabel('Frecuencia (Hz)', fontsize=14)
ax.set_ylabel('Aceleración ' "$(m/s^2)$", fontsize=14)
ax.set_title('Con envolvente')
ax.set_xlim(0,200)
ax.set_ylim(0,0.4)
fig.show()

