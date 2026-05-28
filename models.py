
import numpy as np 


#Calculo de la constante K del modelo W = K L^3.
def calculoconstK(longitudes, pesos):
    Longitudes = np.array(longitudes)
    Pesos = np.array(pesos)

    valoresK = pesos / (longitudes ** 3)
    return np.mean(valoresK)
