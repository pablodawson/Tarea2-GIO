import numpy as np
from scipy.optimize import minimize

# Función objetivo
def funcion_objetivo(params, *args):
    x_, y_, p1, p2, p3, p4, p5 = params
    P = np.array([p1, p2, p3, p4, p5])
    T, W, F = args[0], args[1], args[2]
    return np.sum(P * T * W) + np.sqrt(x_**2 + y_**2) * F

# Restricciones
def restriccion1(params, *args):
    x_, y_, p1,p2,p3,p4,p5 = params
    P = np.array([p1, p2, p3, p4, p5])
    x, y = args[0], args[1]
    K, PR = args[2], args[3]
    return K * P / ((x - x_)**2 + (y - y_)**2) - PR

def restriccion2(params, *args):
    x_, y_,_,_,_,_,_ = params
    xt, yt, rt = args[0], args[1], args[2]
    return (xt - x_)**2 + (yt - y_)**2 - rt**2

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

# Solución del problema de optimización
#P = np.zeros(len(I))  # Potencia irradiada inicializada a cero
initial_guess = np.array([0.001, 0.001, 0,0,0,0,0])

# Definición de las restricciones
cons = [
    {'type': 'ineq', 'fun': restriccion1, 'args': (x, y, K, PR)},
    {'type': 'ineq', 'fun': restriccion2, 'args': (xt, yt, rt)}
]

# Ejecución de la optimización
result = minimize(funcion_objetivo, initial_guess, args=(T, W, F), constraints=cons)

# Obtención de los resultados
x_ = result.x[0]
y_ = result.x[1]
P = result.x[2:]

print("Posición óptima de la torre de comunicaciones:")
print("x_ =", x_)
print("y_ =", y_)
print("Potencia irradiada óptima:", P)
