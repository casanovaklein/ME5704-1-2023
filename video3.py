# se importan librerias
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('dark_background')

# arreglo temporal
t = np.linspace(0, 9, num=10)
t2 = np.arange(0, 10, step=0.5)


#Como crear funciones
x = np.linspace(0, 2*np.pi)
y = np.sin(x)*np.sqrt(x**3)


# Como plotear

fig, ax = plt.subplots()
ax.plot(x, y, label="funcion")
ax.scatter(x, y, label="puntos", c="r", s=20)
ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("esto es un grafico")
fig.show()





# Como plotear
#fig, ax = plt.subplots()
#ax.plot(x, y, label="sin(x)")
#ax.scatter(x, y, c="red", s=20)
#ax.legend()
#ax.set_xlabel("x")
#ax.set_ylabel("y")
#ax.set_title("Funcion sin(x)")
#ax.grid()
#fig.show()


