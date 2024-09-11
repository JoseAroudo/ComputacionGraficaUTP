import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# 1) Crea un array A con valores del 1 al 15. Luego, redimensiona este array a una matriz de 3x5.
A = np.arange(1, 16)
A = A.reshape(3, 5)

# 2) Calcula la suma, la media y el producto de los elementos de A.
suma_A = np.sum(A)
media_A = np.mean(A)
producto_A = np.prod(A)

# 3) Selecciona el segundo y tercer elemento de la segunda fila de A.
elementos_fila_2 = A[1, 1:3]

# 4) Crea un array B que contenga solo los elementos de A que son mayores que 7.
B = A[A > 7]  # Elementos de A mayores a 7


# 5) Calcula el determinante y la inversa de una matriz cuadrada C de 3x3 que crees.
C = np.random.randint(1, 10, size=(3, 3))  # Matriz cuadrada C 3x3
determinante_C = np.linalg.det(C)  # Determinante de C
inversa_C = np.linalg.inv(C)  # Inversa de C


# 6) Dado un array D de 100 números aleatorios, calcula su valor máximo, mínimo, media y desviación estándar.

D = np.random.randn(100)  # Array de 100 números aleatorios
max_D = np.max(D)
min_D = np.min(D)
media_D = np.mean(D)
std_D = np.std(D)

# 7) Grafica la función seno y coseno en el rango de -2π a 2π en el mismo gráfico.
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)  # Rango de -2π a 2π
y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y_sin, label='Seno')
plt.plot(x, y_cos, label='Coseno')
plt.title('Gráfico de las funciones Seno y Coseno')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.legend()
plt.grid(True)
plt.show()

# 8) Usa D para crear un gráfico de dispersión, representando los valores de D contra sus índices.
plt.figure(figsize=(8, 6))
plt.scatter(range(len(D)), D, color='blue')
plt.title('Gráfico de Dispersión de D')
plt.xlabel('Índice')
plt.ylabel('Valor de D')
plt.grid(True)
plt.show()

# 9) Crea un histograma de D, ajustando el número de bins para una mejor visualización.
plt.figure(figsize=(8, 6))
plt.hist(D, bins=20, color='green', alpha=0.7)
plt.title('Histograma de D')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()



# 10)Lee una imagen con Matplotlib, conviértela a escala de grises y muestra ambas imágenes (original y en escala de grises).
ruta= os.getcwd()
rutaFoto= os.path.join(ruta, 'foto.jpg')
print(ruta)
img = mpimg.imread(rutaFoto)
plt.figure(figsize=(6, 6))
plt.imshow(img)
plt.title('Imagen Original')
plt.axis('off')
plt.show()


# Convertir a escala de grises y mostrar
gray_img = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])
plt.figure(figsize=(6, 6))
plt.imshow(gray_img, cmap='gray')
plt.title('Imagen en Escala de Grises')
plt.axis('off')
plt.show()