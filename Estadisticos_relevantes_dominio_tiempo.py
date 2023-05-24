import numpy as np
import scipy.io as sio
import matplotlib.pyplot as plt
plt.style.use('dark_background')

#Leer datos
Datos0=sio.loadmat('datos/estadisticos_relevantes/normal.mat')
Datos2=sio.loadmat('datos/estadisticos_relevantes/inner.mat')
Normal=Datos0['normal']
Inner=Datos2['inner']

#vector de tiempo
Fs=48828 #sampling rate
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



fig, ax = plt.subplots()
ax.plot(t, Inner, label="Falla pista interna")
ax.plot(t, Normal, label="Sin falla")
ax.legend()
ax.set_xlabel("Tiempo [seg]")
ax.set_ylabel("Aceleracion" "$[m/s^2]$")
ax.set_title("Comparación dos señales")
fig.show()

# Define la señal x(t)

# Calcula el valor RMS
rms_normal = np.sqrt(np.mean(Normal**2))
rms_inner = np.sqrt(np.mean(Inner**2))
# Calcula el valor peak
peak_normal = np.max(np.abs(Normal))
peak_inner = np.max(np.abs(Inner))
# Calcula el valor peak-to-peak
ptp_normal = np.max(Normal) - np.min(Normal)
ptp_inner = np.max(Inner) - np.min(Inner)

# Calcula el factor cresta
crest_factor_normal = peak_normal / rms_normal
crest_factor_inner = peak_inner / rms_inner
# Calcula la media
mean_normal = np.mean(Normal)
mean_inner = np.mean(Inner)
# Calcula la varianza
variance_normal = np.var(Normal)
variance_inner = np.var(Inner)
# Calcula la skewness
skewness_normal = np.mean((Normal - mean_normal)**3) / variance_normal**(1.5)
skewness_inner = np.mean((Inner - mean_inner)**3) / variance_inner**(1.5)
# Calcula la kurtosis
kurtosis_normal = np.mean((Normal - mean_normal)**4) / variance_normal**(2)
kurtosis_inner = np.mean((Inner - mean_inner)**4) / variance_inner**(2)

# Imprime los resultados
print("RMS Rodamiento normal: {:.3f}".format(rms_normal))
print("RMS Rodamiento falla pista interna: {:.3f}".format(rms_inner))
print(" ")

print("Valor Peak Rodamiento normal: {:.3f}".format(peak_normal))
print("Valor Peak Rodamiento falla pista interna: {:.3f}".format(peak_inner))
print(" ")

print("Valor Peak-to-Peak Rodamiento normal: {:.3f}".format(ptp_normal))
print("Valor Peak-to-Peak Rodamiento falla pista interna: {:.3f}".format(ptp_inner))
print(" ")

print("Factor Cresta Rodamiento normal: {:.3f}".format(crest_factor_normal))
print("Factor Cresta Rodamiento falla pista interna: {:.3f}".format(crest_factor_inner))
print(" ")

print("Media Rodamiento normal: {:.3f}".format(mean_normal))
print("Media Rodamiento falla pista interna: {:.3f}".format(mean_inner))
print(" ")

print("Varianza Rodamiento normal: {:.3f}".format(variance_normal))
print("Varianza Rodamiento falla pista interna: {:.3f}".format(variance_inner))
print(" ")

print("Skewness Rodamiento normal: {:.3f}".format(skewness_normal))
print("Skewness Rodamiento falla pista interna: {:.3f}".format(skewness_inner))
print(" ")

print("kurtosis Rodamiento normal: {:.3f}".format(kurtosis_normal))
print("kurtosis Rodamiento falla pista interna: {:.3f}".format(kurtosis_inner))


