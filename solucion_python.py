import numpy as np
from scipy.optimize import minimize
import time
import tracemalloc
 
# starting the monitoring
tracemalloc.start()
 
# Conjuntos y parámetros
x = np.array([23, 25, 22, 27, 35])  # Posición x de cada servidor i
y = np.array([30, 31, 28, 32, 19])  # Posición y de cada servidor i
xt, yt = 8, 8  # Posición x e y del centro de la zona restringida
rt = 5  # Radio de la zona restringida [km]
K = 25  # Constante de potencia [G * km^2]
F = 800  # Dólares por kilómetro lineal de fibra [US$/km]
W = 0.0075  # Costo de watt hora [US$/Watt * hour]
PR = 0.025  # Potencia mínima de cada servidor [Watt]
T = 24*10*365  # Tiempo de funcionamiento (en horas)
# Función objetivo ##

def funcion_objetivo(args):
    x_, y_, p1, p2, p3, p4, p5 = args
    P = np.array([p1, p2, p3, p4, p5])
    return np.sum(P * T * W) + np.sqrt(x_**2 + y_**2) * F

# Restricciones
def restriccion1(vars):
    x_, y_, p1,p2,p3,p4,p5 = vars
    P = np.array([p1, p2, p3, p4, p5])
    return (K * P) - PR * ((x_ - xt)**2 + (y_ - yt)**2)

def restriccion2(vars):
    x_, y_, _,_,_,_,_ = vars
    return -(x_ - xt)**2 - (y_ - yt)**2 + rt**2

# Guess inicial
initial_guess = [0.001, 0.001, 0,0,0,0,0]

# Definición de las restricciones
cons = [
    {'type': 'ineq', 'fun': restriccion1},
    {'type': 'ineq', 'fun': restriccion2}
]

start = time.time()
# Ejecución de la optimización
result = minimize(funcion_objetivo, initial_guess, constraints=cons, method='COBYLA')

print("Tiempo de ejecución:", time.time() - start)
# Obtención de los resultados
x_ = result.x[0]
y_ = result.x[1]
P = result.x[2:]

print("Posición óptima de la torre de comunicaciones:")
print("x_ =", x_)
print("y_ =", y_)
print("Potencia irradiada óptima:", P)

print("Memoria ocupada: "+str(tracemalloc.get_traced_memory()))
tracemalloc.stop()