set I := {1, 2, 3, 4, 5}; # Conjunto de servidores

param x{i in I};  # Posición x del servidor i
param y{i in I};  # Posición y del servidor i
param xt;  # Posición x del centro de la zona restringida
param yt;  # Posición y del centro de la zona restringida
param rt;  # Radio de la zona restringida
param K;  # Constante de potencia
param F;  # Dólares por kilómetro lineal de fibra
param W;  # Costo de watt hora
param PR;  # Potencia mínima de cada servidor
param T;  # Tiempo de funcionamiento (en horas)

var x_ >= 0;  # Posición x de la torre de comunicaciones
var y_ >= 0;  # Posición y de la torre de comunicaciones
var P{i in I} >= 0;  # Potencia irradiada al servidor i

minimize FO: (sqrt(x_^2 + y_^2) * F + sum{i in I}(P[i]) * T * W);

subject to Restr1{i in I}: 
    K * P[i] / ((x[i] - x_)^2 + (y[i] - y_)^2) >= PR;
subject to Restr2: 
    (xt - x_)^2 + (yt - y_)^2 <= rt^2;

