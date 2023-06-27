# Ecuación de transferencia radiativa
Solución para la ecuación de Transferencia Radiativa. Este trabajo intenta resolver la Ecuación de Transferencia Radiativa (ETR) con condiciones específicas e iniciales dadas.

La ecuación de transferencia radiativa es una ecuación fundamental en la física que describe la propagación de la radiación a través de un medio, establece cómo cambia la intensidad de la radiación a medida que pasa por este y cómo se ve afectada por diferentes procesos de absorción, emisión y dispersión.

![ETR](https://github.com/LucreciaBeltz/ETR/blob/main/images/radiativa.png)
---

## Contacto
Escuela Nacional de Estudios Superiores ((https://www.unam.mx/))

María Lucrecia Beltz González ([LucreciaBeltz](https://github.com/LucreciaBeltz))

## Licencia
 Copyright © 2023 <lucreciabeltz@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# Introducción
La ecuación de transferencia radiativa surge  para describir cómo la radiación se propaga y se modifica a medida que atraviesa un medio, tomando en cuenta procesos como la absorción (primera parte de la ecuación) y emisión (segunda parte). El cambio de intensidad específica en un rango, se considera la intensidad específica entrante por la opacidad, más la emisibilidad. Esta relación de procesos se expresa en la siguiente ecuación iterativa:
    $I(i+1)(\nu) = (I(i)(\nu) * exp(-tau(\nu))) + (S(\nu) * exp(1-tau(\nu)))$
donde:  
- $I(\nu)$ -> intensidad específica
- $S(\nu)$ -> función fuente 
- $tau(nu)$ -> profundidad óptica
    $I(i)(\nu)$ es la intensidad específica en la capa $i$ a la frecuencia $\nu$.
    $I(i+1)(\nu)$ es la intensidad específica en la capa siguiente ($i+1$) a la frecuencia $\nu$.
    $S(\nu)$ es la función fuente que representa la cantidad de radiación generada o inyectada en el medio a la frecuencia $\nu$.
    $\tau(\nu)$ es la profundidad óptica, que es una medida de cuánto se atenúa o absorbe la radiación a medida que atraviesa el medio. 

    La profundidad óptica en una frecuencia se puede definir como:
        $tau = delta/2( k_i(\nu) + k_(i-1)(\nu))$
        donde $k_i(\nu)$ y $k_{i-1}(\nu)$ son las opacidades en las capas $i$ e $i-1$. Este valor ayuda a determinar si el medio es grueso (cuando es > 1 no se ve) o delgado ópticamente (cuando está entre 0 y 1 sí se ve).

# Objetivos generales
* Programar la ecuación iterativa para resolver la ecuación de transferencia radiativa: 
    $I(i+1)(\nu) = I(i)(\nu) * exp(-tau(\nu)) + S(\nu) * exp(1-tau(\nu))$
* Calcular la intensidad específica bajo condiciones específicas dadas:
    $S_nu:$ Ecuación de planck.
    $k_nu:$ Ecuación (21) de Dulk (1985)
---


# Metodología
Para fines de este trabajo se propone usar a modo de función fuente (S) la ecuación de Planck en términos de la frecuencia, la cual describe la radiación electromagnética emitida por un cuerpo negro en equilibrio térmico en una temperatura definida.
El coeficiente de absorción está dado por la Ecuación 21, Dulk(1985):
    $Kv = 0.2 ne^(2) * T^(-3/2) * v^(-2) cm^(-1)$, y se calcula en función de: 
    * densidad electrónica $(ne)$ 
    * temperatura $T$
    * frecuencia $v$
las condiciones iniciales para este problema se definen de la siguiente manera:
    $nu = 17e9$ Frecuencia en Hz a la que se calcula
    $T = 1e5$ Atmósfera con temperatura constante en grados Kelvin
    $ne = 1e12$ cm-3 densidad constante de electrones
    $delta = 1$ cambio en km, se multiplica por 1e5 para tratar en cm
    $i=[0:51]$ Número de capas (52 capas)
    $I_0 = 0$ Condición de arranque

* Se implementan funciones para cada parte de la ecuación de interés
* Una vez resuelta la ecuación se aplica para todas las capas
* Se almacenan los valores resultantes en listas
* Se usan las listas para graficar 

# Herramientas de software
### Bibliotecas
* [Python 3](https://www.python.org/)
* Linux Ubuntu    64-bit
* [Github](https://www.github.com)
* git

### Paquetes
* [Matplotlib version 3.2.2](https://matplotlib.org/)
* [Numpy version 1.21.5](https://numpy.org/) 
* [Math](https://docs.python.org/3/library/math.html)
* [Astropy](https://docs.astropy.org/en/stable/api/astropy.modeling.physical_models.BlackBody.html)


# Implementación 

### Funciones
* S: Define la ecuación de Planck mediante un evaluador de python *Blackbody*, que pertenece a la biblioteca Astropy.

    Input: T, nu
    Output: S(nu*u.Hz)
 
* tau:  Define la profundidad óptica

    Input: delta, nu, T, ne
    Output: tau

* k: Define la opacidad de la capa con la Ecuación 21, Dulk(1985)

    Input: ne, T, nu
    Output:  k
    
### Listas
* X: Guarda valores de x iterativamente
* Y: Guarda los valores de la intensidad iterativamente
* Z: Guarda los valores de tau iterativamente

### Graficas
* Gráfica de x vs intensidad
* Gráfica de x vs Tau
---


# Pruebas
![ETR](https://github.com/LucreciaBeltz/ETR/blob/main/images/LinXvsI.png)
![ETR](https://github.com/LucreciaBeltz/ETR/blob/main/images/LinXvsT.png)

# Resultados
![ETR](https://github.com/LucreciaBeltz/ETR/blob/main/images/LogXvsI.png)
![ETR](https://github.com/LucreciaBeltz/ETR/blob/main/images/LogXvsT.png)

## Instalación y ejecución
1. clonar el repositorio *ETR*
2. ejecutar el archivo *radiativa.py*
---

## Conclusiones
La intensidad específica depende de las características del medio con el que se impacta, pueden ser tan diversos, y por ello se requiere alta precisión al realizar simulaciones que impliquen la radiación.

## Bibliografía
https://ui.adsabs.harvard.edu/abs/1985ARA%26A..23..169D/abstract
https://es.wikipedia.org/wiki/Ley_de_Planck
https://docs.astropy.org/en/stable/api/astropy.modeling.physical_models.BlackBody.html
https://webs.um.es/bussons/TransfRadiativa.pdf
https://www.scielo.org.mx/pdf/rmfe/v54n1/v54n1a6.pdf

