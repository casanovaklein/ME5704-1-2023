% Generar una señal con ruido gaussiano
Fs = 10000; % Frecuencia de muestreo
t = 0:1/Fs:10; % Vector de tiempo de 1 segundo
f1 = 4; % Frecuencia de la señal
periodo = 1/f1;
s = sin(2*pi*f1*t); % Señal sin ruido
ruido = 0.5*randn(size(t)); % Ruido gaussiano con desviación estándar de 0.5
x = s + ruido; % Señal con ruido


% Aplicar Time Synchronous Averaging
[x_tsa,t_tsa,p,rpm] = tsa(x, Fs, periodo);


% Graficar las señales
figure;
subplot(2,1,1);
plot(t, x);
title('Señal extendida con ruido gaussiano');
%xlim([0, 0.25])
xlabel('Tiempo (s)');
ylabel('Amplitud');
plot_darkmode

subplot(2,1,2);
plot(t_tsa, x_tsa);
hold on
plot(t, x);
hold off
xlim([0, 0.25])
title('Señal promediada con TSA');
xlabel('Tiempo (s)');
ylabel('Amplitud');
plot_darkmode
