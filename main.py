import matplotlib.pyplot as plt
import numpy as np

#EJERCICIO 1
# Datos de la tabla
longitudes = np.array([36.81, 31.77, 43.82, 36.82, 32.07, 45.07, 35.89])
pesos = np.array([0.78, 0.47, 1.16, 0.74, 0.44, 1.40, 0.64])

# Calcular l³ para graficar según la relación W ∝ l³
longitudes_cubicas = longitudes ** 3

# Crear la figura
plt.figure(figsize=(7, 3.5))

# Gráfico de dispersión: Peso vs Longitud³
plt.scatter(longitudes_cubicas, pesos, color='blue', s=80, label='Datos recopilados')

plt.title('Relación entre Peso [W] y Longitud³ [l³] de los pescados')
plt.xlabel('Longitud³ [cm³]')
plt.ylabel('Peso [kg]')
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.savefig("grafica Ejercicio 1.png")
plt.show()


#EJERCICIO 2
