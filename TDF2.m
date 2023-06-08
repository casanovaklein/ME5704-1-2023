function [f,Y]=TDF(x,Fs) %Fs: frecuencia de muestreo; 
Y=fft(x);
L=length(x);
Y=abs(Y/L);
Y=Y(1:round(L/2)+1);
Y(2:end-1)=2*Y(2:end-1);
f=(Fs/L)*(0:L/2);
end
