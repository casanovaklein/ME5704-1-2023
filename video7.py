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

# Señal sinusoidal
# Definir la frecuencia, amplitud y fase de la señal sinusoidal
frecuencia = np.pi/4
amplitud = 3
fase = 0

# Crear un array de tiempo
t = np.linspace(0, 2*np.pi, 1000)

# Crear la señal sinusoidal
y = amplitud * np.sin(2*np.pi*frecuencia*t + fase)

FFT, frec = fast_fourier_transform(t, y)

# Crear la figura y el subplot
fig, axs = plt.subplots(2,1)
# Graficar la señal sinusoidal
axs[0].plot(t, y)
axs[1].stem(frec, FFT)
# Añadir título y etiquetas de los ejes
axs[0].set_title('Señal sinusoidal')
axs[1].set_xlabel('Tiempo')
axs[0].set_ylabel('Amplitud')
axs[1].set_xlim(0, 4)
# Mostrar la gráfica
fig.show()


# señal periodica
# Definir la frecuencia y amplitud de la señal periódica
frecuencia = np.pi/4
amplitud = 1

# Crear un array de tiempo
t = np.linspace(0, 2*np.pi, 1000)

# Crear la señal periódica utilizando la función de onda cuadrada
y = amplitud * np.sign(np.sin(2*np.pi*frecuencia*t))

FFT, frec = fast_fourier_transform(t, y)

# Crear la figura y el subplot
fig, axs = plt.subplots(2,1)
# Graficar la señal sinusoidal
axs[0].plot(t, y)
axs[1].stem(frec, FFT)
# Añadir título y etiquetas de los ejes
axs[0].set_title('Señal periodicas')
axs[1].set_xlabel('Frecuencia')
axs[0].set_ylabel('Amplitud')
axs[1].set_xlim(0, 8)
# Mostrar la gráfica
fig.show()


# señal transiente
# Definir los parámetros de la señal transiente
frecuencia = 10 # Hz
periodo = 1 / frecuencia
tiempo_total = 15 * periodo # segundos

# Crear el vector de tiempo
t = np.arange(0, tiempo_total, 0.001)

# Crear la señal transiente
A = 1
tau = 2*periodo
x = A * np.exp(-t/tau) * np.sin(2*np.pi*frecuencia*t)
FFT, frec = fast_fourier_transform(t, x)

# Hacer el plot de la señal transiente

fig, ax = plt.subplots()

# Graficar la señal periódica
fig, axs = plt.subplots(2,1)
# Graficar la señal sinusoidal
axs[0].plot(t, x)
axs[1].stem(frec, FFT)
# Añadir título y etiquetas de los ejes
axs[0].set_title('Señal transiente')
axs[1].set_xlabel('Tiempo')
axs[0].set_ylabel('Amplitud')
axs[1].set_xlim(0, 40)
# Mostrar la gráfica
fig.show()


# señal ruidosa
# Definir los parámetros de la señal transiente
frecuencia = 10 # Hz
periodo = 1 / frecuencia
tiempo_total = 15 * periodo # segundos

# Crear el vector de tiempo
t = np.arange(0, tiempo_total, 0.001)

# Crear la señal transiente
A = 1
tau = 2*periodo
x = A * np.exp(-t/tau) * np.sin(2*np.pi*frecuencia*t)

# Agregar ruido a la señal
ruido_amplitud = 0.2 # amplitud del ruido
ruido = ruido_amplitud * np.random.randn(len(t))
x_ruidosa = x + ruido

FFT, frec = fast_fourier_transform(t, x_ruidosa)
# señal ruidosa
fig, ax = plt.subplots()

# Graficar la señal periódica
# Graficar la señal periódica
fig, axs = plt.subplots(2,1)
# Graficar la señal sinusoidal
axs[0].plot(t, x_ruidosa)
axs[1].stem(frec, FFT)
# Añadir título y etiquetas de los ejes
axs[0].set_title('Señal transiente')
axs[1].set_xlabel('Tiempo')
axs[0].set_ylabel('Amplitud')
axs[1].set_xlim(0, 40)
# Mostrar la gráfica
fig.show()


# señal con modulacion
# Definir los parámetros de la señal portadora y moduladora

m = 0.6 # factor que acompana al coseno
A = 10 # amplitud
f_p = 25 # frecuencia de la senal portadora
f_m = 2 # frecuecnia de la senal modulada
dt = 0.01 # discretisacion en seg
N = 200 # numero de pasos
T = dt*N # tiempo final
fs = 1/dt # frecuencia de muestreo

t = np.arange(0, T, dt) # vector temporal
x_p = A*np.sin(2*np.pi*f_p*t)
x_m = (1 + m*np.cos(2*np.pi*f_m*t))
x = x_p*x_m

FFT, frec = fast_fourier_transform(t, x)

# plots..

fig, ax = plt.subplots()
ax.plot(t, x, label = 'Dominio temporal')
ax.set_xlabel('Tiempo [seg]')
ax.set_ylabel('Amplitud')
ax.set_ylim(-20, 20)
ax.set_xlim(0,2)
ax.grid()
fig.legend()
fig.show()

fig, ax = plt.subplots()
ax.stem(frec, FFT, label='Dominio en frecuencias')
ax.grid()
ax.set_xlabel('Frecuencia [Hz]')
ax.set_ylabel('Amplitud')
ax.set_xlim(0, 50)
ax.set_ylim(0, 12)
ax.text(25.5, 10.5, r'$f_p = 25 hz$, amplitud de 10')
ax.text(28, 3, r'Ancho de banda igual a la frecuencia moduladora $f_m = 2 hz$', wrap=True)
fig.legend()
fig.show()

