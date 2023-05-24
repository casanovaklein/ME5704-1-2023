import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generamos datos de ejemplo
n = 100
t = np.linspace(0, 10, n)
z = np.random.randn(n) + np.random.randn(n)*1j

# Creamos una figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extraemos la parte real, imaginaria y el tiempo de los números complejos
x = z.real
y = z.imag

# Creamos el gráfico 3D
ax.plot(x, y, t)

# Etiquetamos los ejes
ax.set_xlabel('Parte real')
ax.set_ylabel('Parte imaginaria')
ax.set_zlabel('Tiempo')

# Mostramos el gráfico
plt.show()
