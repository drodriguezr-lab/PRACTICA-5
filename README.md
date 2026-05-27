## PRACTICA-5 Modelos De Similitud Geométrica

# El Problema del Campeonato de Pesca De Róbalo
Imaginemos que la competencia premia al pez más pesado, pero la única herramienta con la que contamos paradeterminar el peso de los peces es una cinta métrica. Como en las versiones anteriores del campeonato asistieron miles de participantes queremos poder predecir el peso de un pescado en término de algunas dimensiones fáciles de medir. A pesar de que el peso de un pescado se ve afectado por variables como la forma del pescado,la densidad del pescado, la edad del pescado, entre otras, haremos un modelo que dependa 
solo de variables medibles por nuestra cinta métrica. Algunos de los supuestos que usaremos en nuestro modelo son que:
* la especie está fija y todos los pescados serán robalos. (En general esto sí sucede en
los campeonatos).
* la densidad de los pescados es constante. (Esto es poco realista pero nos servirá
para un primer modelo).
* las variables como la estación del año, el sexo, la edad, etc. no afectan al peso del
róbalo.
* los róbalos son geométricamente similares.

##  INTEGRANTES 
* Rodríguez Rodríguez Diego


## Uso e instalación
Instalamos los siguientes paquetes:
1. `numpy` como np
2. `matplotlib.pyplot` como `plt`



## Ejercicio 1

Para poder ajustar nuestro modelo necesitamos datos sobre el peso (W) y la longitud (l) de algunos pescados. Los únicos datos sobrevivientes de los campeonatos anteriores se encuentran en la siguiente tabla:
| Longitud (cm) | 36.81|31.77|43.82|36.82|32.07|45.07|35.89|
| ------------ | ----- |--- |--- |--- |--- |--- |--- |
| Peso (kg) | .78 |.47 |1.16 |.74 |.44 |1.4 |.64  |


En realidad, lo que medimos cuando "pesamos" en kg es la masa, y no el peso, de lo que 
estemos midiendo.
Grafica los datos de esta tabla de acuerdo a la relación:
$W \propto l ^3$

![Gráfica de relación $W y l^3$](media/grafica Ejercicio 1.png)




## Ejercicio 2
Utiliza los datos anteriores y el método de tu preferencia para estimar un buen valor de K
para nuestro modelo de similaridad geométrica $W = Kl^3$
. Grafica la estimación contra los 
datos. ¿Qúe tan bueno es el ajuste? ¿Hay algún efecto que nuestro modelo no capture?

Hint: usa la libreria numpy

## Ejercicio 3


Ahora añadiremos una dimensión extra a nuestra tabla anterior. Supongamos que además de los datos anteriores también tenemos disponible la circunferencia máxima de cada pez.
|Cicunferencia Máxima|24.77|21.29|27.94|21.59|31.75|22.86|
|-----|----|-----|-----|-----|----|----|

Realice el ajuste del nuevo modelo en términos de la circunferencia ¿Cómo queda la fórmula explicita del modelo?¿Qué tan bueno es el ajuste?

El nuevo modelo:

## $W=k l C_m^2$

## Conclusiones 

