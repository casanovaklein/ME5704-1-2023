clear; clc
datos_inner = load('C:\Users\Essteban\Desktop\Semestre otoño 2023\Auxiliar mantenimiento predicitvo\github\ME5704-1-2023\datos\estadisticos_relevantes\inner.mat');
datos_normal = load('C:\Users\Essteban\Desktop\Semestre otoño 2023\Auxiliar mantenimiento predicitvo\github\ME5704-1-2023\datos\estadisticos_relevantes\normal.mat');

vib_inner = datos_inner.inner;
vib_normal = datos_normal.normal;
Fs = 48828;
delta_t = 1/Fs;
t = 0:delta_t:((length(vib_inner)-1)*delta_t);

kurtogram(vib_normal,Fs)