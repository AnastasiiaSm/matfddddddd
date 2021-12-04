import math
import matplotlib.pyplot as plt
import numpy as np
#Границы
a = 0
b = 145
#Шаг 
h = 5

k=0
V0=1000
c=math.pi/4
#Дифференциальное уравнение
def f(t,x,Vx):
    return (Vx)

def g(t,x,Vx):
    return 0

#Массивы для хранения значений
Runge_Kutta_x = []
Runge_Kutta_Vx = []

t = np.arange(a, b+h, h, dtype=float)

#Начальное условие
Runge_Kutta_x.append(0)
Runge_Kutta_Vx.append(math.cos(c)*V0)

#Метод Рунге-Кутта
for i in range(int((b-a)/h)):
    K1 = h*f(t[i], Runge_Kutta_x[i], Runge_Kutta_Vx[i])
    L1 = h*g(t[i], Runge_Kutta_x[i], Runge_Kutta_Vx[i])
    K2 = h*f(t[i] + 0.5*h, Runge_Kutta_x[i] + 0.5*K1, Runge_Kutta_Vx[i] + 0.5*L1)
    L2 = h*g(t[i] + 0.5*h, Runge_Kutta_x[i] + 0.5*K1, Runge_Kutta_Vx[i] + 0.5*L1)
    K3 = h*f(t[i] + 0.5*h, Runge_Kutta_x[i] + 0.5*K2, Runge_Kutta_Vx[i] + 0.5*L2)
    L3 = h*g(t[i] + 0.5*h, Runge_Kutta_x[i] + 0.5*K2, Runge_Kutta_Vx[i] + 0.5*L2)
    K4 = h*f(t[i] + h, Runge_Kutta_x[i] + K3, Runge_Kutta_Vx[i] + L3)
    L4 = h*g(t[i] + h, Runge_Kutta_x[i] + K3, Runge_Kutta_Vx[i] + L3)
    Runge_Kutta_x.append(Runge_Kutta_x[i] +1/6*(K1 + 2*K2 + 2*K3 + K4))
    Runge_Kutta_Vx.append(Runge_Kutta_Vx[i] +1/6*(L1 + 2*L2 + 2*L3 + L4))

print("t: ", t)
print("Runge-Kutta x: ", Runge_Kutta_x)
print("Runge-Kutta Vx: ", Runge_Kutta_Vx)



#Построение графика
plt.title("Функция y(x)")
plt.xlabel("t")
plt.ylabel("x")
plt.grid()
plt.plot(t, Runge_Kutta_x)
plt.plot(t, Runge_Kutta_Vx)
plt.legend(['x', 'Vx'])
plt.show()