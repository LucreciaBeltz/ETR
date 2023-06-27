import math
import matplotlib 
import matplotlib.pyplot as plt
from astropy.modeling import models
from astropy import units as u

# I(i+1)(nu) = I(i)(nu) * exp(-tau(nu)) + S(nu) * exp(1-tau(nu))

# I(nu) -> es la intensidad específica,
# S(nu) -> función fuente
# tau(nu) -> profundidad óptica: tau = delta/2( k_i(nu) + k_(i-1)(nu))
#     delta -> paso de integración
#     k(nu) -> opacidad en la i-esima capa.

# Calcular intensidad específica con las condiciones:

#    S_nu: Ecuación de planck.
#    k_nu: Ecuación (21) de Dulk (1985)
#    eq 21 Dulk -> Kv = 0.2 ne^(2) * T^(-3/2) * v^(-2) cm^(-1)

# Condiciones iniciales
nu = 17e9 #Hz
T = 1e5 #°K (atmosfera con temperatura constante)
ne = 1e12 #cm-3 #(densidad constante)
delta = 1 * 1e5  #km
capas = 52 #[0:51] #(52 capas)
I_0 = 0 #(condición de arranque)

def S(T, nu):
    S = models.BlackBody(temperature = T * u.K)
    return S(nu*u.Hz)
 
def tau(delta, nu, T, ne):
    tau = delta/2.0 * (k(ne, T, nu) + k(ne, T, nu)) # no entendí como hacer ki y ki-1, por eso tau es constante
    return tau
    #print(tau)

def k(ne, T, nu):
    # Ecuación 21 de Dulk,1985
    #    Kv = 0.2 ne^(2) * T^(-3/2) * v^(-2) cm^(-1)
    k = 0.2 * (ne **2) * (T**(-3/2)) * (nu**(-2)) #cm-1
    return k

i=1
x0 = 0.0

X = []
Y = []
Z = []

for i in range(capas):
    x =  i * delta
    t = tau(delta, nu, T, ne)
    I = I_0 * math.exp(-t) + S(T,nu)*(math.exp(1-t)) 
    X.append(x)
    Y.append(I.value)
    Z.append(t)
    I_0 = I
    #print(i,I)
    x0 = x
#print (X)
#print(Y)

fig, ax = plt.subplots()
ax.plot(X, Y)
ax.set_xscale("linear")
ax.set_yscale("linear")
plt.title('Gráfica de X vs Intensidad')
plt.show()

fig, ax = plt.subplots()
ax.plot(X, Z)
ax.set_xscale("linear")
ax.set_yscale("linear")
plt.title('Gráfica de X vs Tau')
plt.show()
