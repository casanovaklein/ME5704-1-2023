clear; clc
datos_inner = load('C:\Users\Essteban\Desktop\Semestre otoño 2023\Auxiliar mantenimiento predicitvo\github\ME5704-1-2023\datos\estadisticos_relevantes\inner.mat');
datos_normal = load('C:\Users\Essteban\Desktop\Semestre otoño 2023\Auxiliar mantenimiento predicitvo\github\ME5704-1-2023\datos\estadisticos_relevantes\normal.mat');

vib_inner = datos_inner.inner;
vib_normal = datos_normal.normal;
Fs = 48828;
delta_t = 1/Fs;
t = 0:delta_t:((length(vib_inner)-1)*delta_t);


figure
plot(t', vib_inner)
xlabel ('Tiempo [s]')
ylabel('Amplitud [m/s^2]')
title('Aceleración rodamiento falla pista interna')
plot_darkmode


% Cálculo de la STFT
[S_inner, F_inner, T_inner] = stft(vib_inner, Fs, FFTLength = 8096);
[S_normal, F_normal, T_normal] = stft(vib_normal, Fs, FFTLength= 8096);

% Graficar espectrograma de vib_inner
figure
imagesc(T_inner, F_inner, 10*log10(abs(S_inner)));
ylim([0 2000]);  % Establecer límites en el eje y
xlim([0 0.25]);
colorbar;  % Mostrar barra de color
title('Espectrograma de vib\_inner');
xlabel('Tiempo (s)');
ylabel('Frecuencia (Hz)');
plot_darkmode


% Graficar espectrograma de vib_normal
figure
imagesc(T_normal, F_normal, 10*log10(abs(S_normal)));
ylim([0 2000]);  % Establecer límites en el eje y
xlim([0 0.25])
colorbar;  % Mostrar barra de color
title('Espectrograma de vib\_normal');
xlabel('Tiempo (s)');
ylabel('Frecuencia (Hz)');
plot_darkmode
