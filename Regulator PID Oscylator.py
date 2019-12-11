import matplotlib.pyplot as plt

T = 15
xSet = 0.7
xSetLine = [xSet]
h = 0.01
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

    u.append(U)

    x.append(x[i - 1] + h * (y[i - 1] + x[i-1]*(1-x[i-1]*x[i-1]-y[i-1]-y[i-1])))
    y.append(y[i - 1] + h * (-x[i] + y[i-1]*(1-x[i]*x[i]-y[i-1]-y[i-1]) + u[i - 1]))
    error.append(xSet - x[i])

    errorSum += xSet - x[i]
    sqrErrorSum += (xSet - x[i])*(xSet - x[i])
    errorD.append((error[i] - error[i - 1]) / h)
    t.append(t[i - 1] + h)
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

#plt.figure()
#plt.subplot(3, 1, 1)
#plt.plot(t, PArray, color='red')
#plt.xlabel("t")
#plt.ylabel("P")
#plt.subplot(3, 1, 2)
#plt.plot(t, IArray, color='green')
#plt.xlabel("t")
#plt.ylabel("I")
#plt.subplot(3, 1, 3)
#plt.plot(t, DArray, color='blue')
#plt.xlabel("t")
#plt.ylabel("D")
plt.show()
