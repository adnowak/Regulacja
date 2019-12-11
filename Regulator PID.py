import matplotlib.pyplot as plt

T = 1080
xSet = 180
xSetLine = [xSet]
h = 0.1
a = -0.01
x = [200]
u = [0]
t = [0]
error = [x[0] - xSet]
errorSum = error[0]
errorD = [0]

maxPower = 10
basePower = 3
k1 = 0.1
k2 = 0.0001
k3 = 0.1

delay = 5
delayedIterations = int(delay / h)

for i in range(1, int(T / h)):
    P = k1 * basePower * (xSet - x[i - 1])
    I = k2 * basePower * errorSum
    D = k3 * basePower * errorD[i-1]
    U = P + I + D

    if (U > 0) & (U < maxPower):
        u.append(U)
    elif U > 0:
        u.append(maxPower)
    else:
        u.append(0)

    if i > delayedIterations:
        x.append(x[i - 1] + h * (a * x[i - 1] + u[i - 1 - delayedIterations]))
    else:
        x.append(x[i - 1] + h * (a * x[i - 1] + u[i - 1]))
    error.append(xSet - x[i])
    errorSum += xSet - x[i]
    errorD.append((error[i]-error[i-1])/h)
    t.append(t[i - 1] + h)
    if i > int(T / h) / 2:
        xSet = 200
        if i > int(T / h) * 0.7:
            xSet = 150

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
plt.plot(error, u, color='blue')
plt.xlabel("error")
plt.ylabel("u")
plt.show()
