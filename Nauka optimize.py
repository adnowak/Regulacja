import numpy as np
from scipy.optimize import minimize


def calcVolume(x):
    length = x[0]
    width = x[1]
    height = x[2]
    volume = length*width*height
    return volume


def calcSurface(x):
    length = x[0]
    width = x[1]
    height = x[2]
    surface = 2*(length*width+length*height+width*height)
    return surface


def objective(x):
    return -calcVolume(x)


def constraint(x):
    return 10 - calcSurface(x)


cons = ({'type': 'ineq', 'fun': constraint})

lengthGuess = 1
widthGuess = 1
heightGuess = 1

x0 = np.array([lengthGuess, widthGuess, heightGuess])

sol = minimize(objective, x0, method='SLSQP', constraints=cons, options={'disp': True})

xOpt = sol.x
volumeOpt = -sol.fun
surfaceOpt = calcSurface(xOpt)

print("Lenght: " + str(xOpt[0]))
print("Width: " + str(xOpt[1]))
print("Height: " + str(xOpt[2]))
print("Volume: " + str(volumeOpt))
print("Surface area: " + str(surfaceOpt))
