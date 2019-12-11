import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize

T = 15

h = 0.01
k1Start = 1
k2Start = 1
k3Start = 1
k = np.array([k1Start, k2Start, k3Start])

delay = 0
delayedIterations = int(delay / h)

def work(K):
    sqrErrorSum = 0
    xSet = 0.5
    x = [2]
    y = [0]
    u = [0]
    t = [0]
    PArray = [0]
    IArray = [0]
    DArray = [0]
    error = [x[0] - xSet]
    errorSum = error[0]
    errorD = [0]
    xSetLine = [xSet]

    for i in range(1, int(T / h)):
        P = K[0] * (xSet - x[i-1])
        PArray.append(P)
        I = K[1] * errorSum
        IArray.append(I)
        D = K[2] * errorD[i-1]
        DArray.append(D)
        U = P + I + D
        U =0

        u.append(U)

        x.append(x[i - 1] + h * (y[i - 1] + x[i-1]*(1-x[i-1]*x[i-1]-y[i-1]*y[i-1])))
        y.append(y[i - 1] + h * (-x[i] + y[i-1]*(1-x[i]*x[i]-y[i-1]*y[i-1]) + u[i - 1]))
        error.append(xSet - x[i])
        if error[i] == 0:
            errorSum = 0

        errorSum += xSet - x[i]
        sqrErrorSum += (xSet - x[i])*(xSet - x[i])
        errorD.append((error[i] - error[i - 1]) / h)
        t.append(t[i - 1] + h)
        xSetLine.append(xSet)
    return t, x, y, u, error, xSetLine, sqrErrorSum, PArray, IArray, DArray


def objective(parameters):
    return work(parameters)[6]


sol = minimize(objective, k, method='SLSQP', options={'disp': True})
k1 = sol.x[0]
k2 = sol.x[1]
k3 = sol.x[2]
print("k1= " + str(k1))
print("k2= " + str(k2))
print("k3= " + str(k3))

result = work(np.array([k1, k2, k3]))
t = result[0]
x = result[1]
y = result[2]
u = result[3]
error = result[4]
xSetLine = result[5]
sqrErrorSum = result[6]
PArray = result[7]
IArray = result[8]
DArray = result[9]
print("Sum of squared error= " + str(sqrErrorSum))

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
plt.show()
