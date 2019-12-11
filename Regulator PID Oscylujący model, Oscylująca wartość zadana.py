import math

import matplotlib.pyplot as plt

T = 100
xSet = 0.7
xSetLine = [xSet]
h = 0.01
a = 1
x = [0.71]
y = [0.71]
u = [0]
t = [0]
PArray = [0]
IArray = [0]
DArray = [0]
error = [x[0] - xSet]
errorSum = error[0]
errorD = [0]

basePower = 10
k1 = 0.2
k2 = 0.1
k3 = 0.001

delay = 0.09
delayedIterations = int(delay / h)

for i in range(1, int(T / h)):
    index = max(0, i-1-delayedIterations)
    P = k1 * basePower * (xSet - x[index])
    PArray.append(P)
    I = k2 * basePower * errorSum
    IArray.append(I)
    D = k3 * basePower * errorD[index]
    DArray.append(D)
    U = P + I + D

    u.append(U)

    x.append(x[i - 1] + h * (y[i - 1] + u[i-1]))
    y.append(y[i - 1] + h * (-x[i]))
    error.append(xSet - x[i])
    if error[i] == 0:
        errorSum = 0
    errorSum += xSet - x[i]
    errorD.append((error[i]-error[i-1])/h)
    t.append(t[i - 1] + h)
    xSet = 20*math.sin(t[i-1])
    xSetLine.append(xSet)

plt.subplot(3, 1, 1)
plt.plot(t, x, color='red')
plt.plot(t, xSetLine, color='green', linewidth=1.0)
plt.xlabel("t")
plt.ylabel("x")
plt.subplot(3, 1, 2)
plt.plot(t, u, color='green')
plt.xlabel("t")
plt.ylabel("u")
plt.subplot(3, 1, 3)
plt.plot(t, error, color='blue')
plt.xlabel("t")
plt.ylabel("e")
plt.figure()
plt.subplot(3, 1, 1)
plt.plot(t, PArray, color='red')
plt.xlabel("t")
plt.ylabel("P")
plt.subplot(3, 1, 2)
plt.plot(t, IArray, color='green')
plt.xlabel("t")
plt.ylabel("I")
plt.subplot(3, 1, 3)
plt.plot(t, DArray, color='blue')
plt.xlabel("t")
plt.ylabel("D")
plt.show()
