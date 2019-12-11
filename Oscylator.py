import matplotlib.pyplot as plt

a = 1
b = 1
T = 10
h = 0.1
t = [0]
x = [2]
y = [0]

for i in range(1, int(T / h)):
    x.append(x[i - 1] + h * (y[i - 1] + x[i - 1] * (1 - x[i - 1] * x[i - 1] - y[i - 1] - y[i - 1])))
    y.append(y[i - 1] + h * (-x[i] + y[i - 1] * (1 - x[i] * x[i] - y[i - 1] - y[i - 1])))

    t.append(t[i - 1] + h)

plt.subplot(2, 1, 1)
plt.plot(t, x, color='red')
plt.xlabel("t")
plt.ylabel("x")
plt.subplot(2, 1, 2)
plt.plot(t, y, color='blue')
plt.xlabel("t")
plt.ylabel("y")
plt.show()
