
import numpy as np
import matplotlib.pyplot as plt

# Función y derivada
def f(x):
    return np.sin(x)

def df(x):
    return np.cos(x)

# Dominio principal de la función seno
x = np.linspace(-0.5, 2 * np.pi, 400)
y = f(x)

# Puntos donde se calculan las tangentes
puntos = [0, np.pi/4, np.pi/2, np.pi, 3*np.pi/2]
etiquetas = [
    r"Tangente en $x=0$",
    r"Tangente en $x=\pi/4$",
    r"Tangente en $x=\pi/2$",
    r"Tangente en $x=\pi$",
    r"Tangente en $x=3\pi/2$"
]

colores = ['red', 'green', 'blue', 'magenta', 'cyan']

plt.figure(figsize=(12, 5))

# Curva seno
plt.plot(x, y, color='black', linewidth=3, label='f(x) = sin(x)')

# Rectas tangentes
delta = 1  # controla qué tan largas son las tangentes

for x0, c, label in zip(puntos, colores, etiquetas):
    y0 = f(x0)
    pendiente = df(x0)

    xt = np.linspace(x0 - delta, x0 + delta, 50)
    yt = pendiente * (xt - x0) + y0

    plt.plot(xt, yt, color=c, linewidth=2, label=label)
    plt.scatter(x0, y0, color=c, s=80)

# Líneas de referencia
plt.axhline(0, color='gray', linewidth=1)
plt.axvline(0, color='gray', linewidth=1)

# Límites solicitados
plt.ylim(-1.2, 1.5)
plt.xlim(-0.5, 2 * np.pi)

# Estilo
plt.grid(alpha=0.3)
plt.title('Rectas tangentes a f(x) = sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.tight_layout()

plt.show()
