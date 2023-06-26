# Ecuación de transferencia radiativa
Solución para la ecuación de Transferencia Radiativa
---

# Definición de proyecto
Este trabajo intenta resolver la Ecuación de Transferencia Radiativa (ETR) con condiciones específicas e iniciales dadas.

La ecuación de transferencia radiativa es una ecuación fundamental en la física que describe la propagación de la radiación a través de un medio, establece cómo cambia la intensidad de la radiación a medida que pasa por este y cómo se ve afectada por diferentes procesos de absorción, emisión y dispersión.

![ETR](https://github.com/LucreciaBeltz/ETR/blob/main/images/radiativa.png)
---

# Objetivos generales
    * Programar la ecuación iterativa para resolver la ecuación de transferencia radiativa: 
        $I(i+1)(nu) = I(i)(nu) * exp(-tau(n u)) + S(nu) * exp(1-tau(nu))$
    * Calcular la intensidad específica con las siguientes condiciones:
        $S_nu:$ Ecuación de planck.
        $k_nu:$ Ecuación (21) de Dulk (1985).
        con las siguientes condiciones iniciales:
        $nu = 17e9 Hz$
        $T = 1e5K$ (atmosfera con temperatura constante)
        $ne = 1e12 cm-3$ (densidad constante)
        $delta = 1km$
        $i=[0:51]$ (52 capas)
        $I_0 = 0$ (condición de arranque)
---
    
# Herramientas de software a utilizar
### Bibliotecas:
* [Python 3](https://www.python.org/)
* Linux Ubuntu    64-bit
* [Github](https://www.github.com)
* git

### Paquetes:
* [Matplotlib version 3.2.2](https://matplotlib.org/)
* [Numpy version 1.21.5](https://numpy.org/) 
* [Math](https://docs.python.org/3/library/math.html)
* [Astropy](https://docs.astropy.org/en/stable/api/astropy.modeling.physical_models.BlackBody.html)
---

# Contacto
* María Lucrecia Beltz González ([LucreciaBeltz](https://github.com/LucreciaBeltz))

____
# License :
 Copyright © 2023 <lucreciabeltz@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
____
# Instalación y ejecución
---
1. clonar el repositorio *ETR*
3. ejecutar el archvo *radiativa.py*
____
# Introducción :
La radiación que choca con un cuerpo (absorción) suele cambiar una vez salga de él (emisión). Esto es lo que dice la ETR, en la cuál participan parámetros importantes, como son la intensidad específica de entrada, la función de opacidad del objeto con el que impacta, entre otros.

$I(i+1)(nu) = I(i)(nu) * exp(-tau(n u)) + S(nu) * exp(1-tau(nu))$

donde:  
- $I(nu)$ -> intensidad específica,
- $S(nu)$ -> función fuente 
- $tau(nu)$ -> profundidad óptica

La ecuación anterior, es la ecuación iterativa para calcular el cambio en la intensidad específica, por ello se compone de de 2 partes: la primera que tiene que ver con la absorción $I(i)(nu) * exp(-tau(nu))$, y la segunda con la emisión $S(nu) * exp(1-tau(nu))*.$

Para fines de este trabajo, se propone usar a modo de 



# Metodología:
---
Para fines de este trabajo, se propone usar a modo de función fuente (S) la escuación de Planck en términos de la frecuencia

Ecuación 21, Dulk(1985)


# Implementación 
formula
Astropy -> planck
funcion fuente -> dulk
función Tau

Output:  

Graficas



# Pruebas
---
tau? 
que pasa con k y k-1


# Resultados
---
adjuntar graficas

# Conclusiones
---


# Bibliografía
---
