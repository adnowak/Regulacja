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
pUp = 10
pDown = 10

power = -2.11

heat = False
if x[0] < xSet:
    heat = True
    u[0] = (-1) * power

for i in range(1, int(T / h)):
    if heat:
        if x[i-1] > xSet+pUp:
            heat = False
            u.append(0)
        else:
            u.append((-1) * power)
    else:
        if x[i-1] < xSet-pDown:
            u.append((-1) * power)
            heat = True
        else:
            u.append(0)

    x.append(x[i - 1] + h * (a * x[i - 1] + u[i - 1]))
    error.append(xSet - x[i])
    t.append(t[i - 1] + h)
    if i > int(T / h)/2:
        xSet = 200
        if i > int(T / h)*0.7:
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
