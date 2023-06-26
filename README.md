# ETR
Solución para la ecuación de Transferencia Radiativa

# Ecuación de transferencia radiativa
---

# Definición de proyecto
---
Este trabajo intenta resolver la Ecuación de Transferencia Radiativa (ETR) con condiciones específicas e iniciales dadas.

La ecuación de transferencia radiativa es una ecuación fundamental en la física que describe la propagación de la radiación a través de un medio, establece cómo cambia la intensidad de la radiación a medida que pasa por este y cómo se ve afectada por diferentes procesos de absorción, emisión y dispersión.

![ETR](https://github.com/LucreciaBeltz/ETR/blob/main/images/radiativa.png)

---
'''
path_arqui_image = 'images/radiativa.png'
st.image(path_arqui_image)
'''
---
# Objetivos generales
---
* Programar la ecuación iterativa para resolver la ecuación de transferencia radiativa: 
    I(i+1)(nu) = I(i)(nu) * exp(-tau(n u)) + S(nu) * exp(1-tau(nu))
* Calcular la intensidad específica con las siguientes condiciones:
    S_nu: Ecuación de planck.
    k_nu: Ecuación (21) de Dulk (1985).
    con las siguientes condiciones iniciales:
    nu= 17e9 Hz
    T = 1e5K (atmosfera con temperatura constante)
    ne= 1e12 cm-3 (densidad constante)
    delta=1km
    i=[0:51] (52 capas)
    I_0 = 0 (condición de arranque)
    
# Herramientas de software a utilizar
___
# Libraries:
---
* [Python 3](https://www.python.org/)
* Linux Ubuntu    64-bit
* [Github](https://www.github.com)
* git

# Packages:
* [Matplotlib version 3.2.2](https://matplotlib.org/)
* [Numpy version 1.21.5](https://numpy.org/) 
* [Math]
* [Astropy]

*# Arquitectura general del sistema

*# Fuente de datos

*# Test para adquisición de datos

---

# Contacto
* María Lucrecia Beltz González ([LucreciaBeltz](https://github.com/LucreciaBeltz))

____
# License :
 GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

____
# Instalación y ejecución
---
1. clonar el repositorio *ETR*
3. ejecutar el archvo *ETR.py*
____
# Introducción :
La radiación que choca con un cuerpo (absorción) suele cambiar una vez salga de él (emisión). Esto es lo que dice la ETR, en la cuál participan parámetros importantes, como son la intensidad específica de entrada, la función de opacidad del objeto con el que impacta, entre otros.

## I(i+1)(nu) = I(i)(nu) * exp(-tau(n u)) + S(nu) * exp(1-tau(nu))

donde:  I(nu) -> intensidad específica,
        S(nu) -> función fuente 
        tau(nu) -> profundidad óptica

La ecuación anterior, es la ecuación iterativa para calcular el cambio en la intensidad específica, por ello se compone de de 2 partes: la primera que tiene que ver con la absorción *I(i)(nu) * exp(-tau(nu))*, y la segunda con la emisión *S(nu) * exp(1-tau(nu))*.

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
