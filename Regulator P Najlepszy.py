import matplotlib.pyplot as plt
import numpy
import random

generationsAmount = 20
solutionsPerPop = 20
genomeSize = 1
populationSize = (solutionsPerPop, genomeSize)
unfitness = [0] * solutionsPerPop
genomes = numpy.random.uniform(low=-0.5, high=0.5, size=populationSize)
oldGenomes = numpy.zeros(populationSize)
lowestUnfitness = -1
lowestUnfitnessIndex = 0

T = 1080
xStart = 200
xSet = 180
xSetLine = [xSet]
h = 0.1
a = -0.01
x = [xStart]
u = [0]
t = [0]
error = [xStart - xSet]
unfitness.append(error[0])
errorTotal = []

power = 1

delay = 10
delayedIterations = int(delay/h)

for generation in range(0, generationsAmount):
    unfitness = [error[0]]
    for solution in range(0, solutionsPerPop):
        unfitness.append(0)
        for i in range(1, int(T / h)):
            P = genomes[solution][0] * power * (xSet - x[i - 1])

            if P > 0:
                u.append(P)
            else:
                u.append(0)

            if i > delayedIterations:
                x.append(x[i - 1] + h * (a * x[i - 1] + u[i - 1 - delayedIterations]))
            else:
                x.append(x[i - 1] + h * (a * x[i - 1] + u[i - 1]))
            error.append(xSet - x[i])
            unfitness[solution] = unfitness[solution] + abs(error[i])
            t.append(t[i - 1] + h)
            if i > int(T / h) / 2:
                xSet = 200
                if i > int(T / h) * 0.7:
                    xSet = 150
        xSet = 180
        x.clear()
        x = [xStart]
        t.clear()
        t = [0]
        u.clear()
        u = [0]
        error.clear()
        error = [xStart - xSet]
        if lowestUnfitness > 0:
            if unfitness[solution] < lowestUnfitness:
                lowestUnfitness = unfitness[solution]
                lowestUnfitnessGenome = genomes[solution].copy()
        else:
            lowestUnfitness = unfitness[solution]
            lowestUnfitnessGenome = genomes[solution].copy()
    oldGenomes = genomes.copy()
    genomes.fill(0)
    for i in range(0, solutionsPerPop, 2):
        nextSolution1Genome = []
        nextSolution2Genome = []
        solution1Index = random.randint(0, solutionsPerPop-1)
        solution1Genome = oldGenomes[solution1Index]
        solution1Unfitness = unfitness[solution1Index]
        solution2Index = random.randint(0, solutionsPerPop-1)
        solution2Genome = oldGenomes[solution2Index]
        solution2Unfitness = unfitness[solution2Index]
        solution3Index = random.randint(0, solutionsPerPop-1)
        solution3Genome = oldGenomes[solution3Index]
        solution3Unfitness = unfitness[solution3Index]
        solution4Index = random.randint(0, solutionsPerPop-1)
        solution4Genome = oldGenomes[solution4Index]
        solution4Unfitness = unfitness[solution4Index]
        if solution1Unfitness < solution2Unfitness:
            if solution3Unfitness < solution4Unfitness:
                genomeBaseP = solution1Genome[0] + solution3Genome[0]
            else:
                genomeBaseP = solution1Genome[0] + solution4Genome[0]
        else:
            if solution3Unfitness < solution4Unfitness:
                genomeBaseP = solution2Genome[0] + solution3Genome[0]
            else:
                genomeBaseP = solution2Genome[0] + solution4Genome[0]
        nextSolution1Genome.append((genomeBaseP + random.gauss(0, genomeBaseP / 10)) / 2)
        nextSolution2Genome.append((genomeBaseP + random.gauss(0, genomeBaseP / 10)) / 2)
        genomes[i] = nextSolution1Genome
        genomes[i + 1] = nextSolution2Genome
for i in range(1, int(T / h)):
    P = lowestUnfitnessGenome[0] * power * (xSet - x[i - 1])

    if P > 0:
        u.append(P)
    else:
        u.append(0)

    if i > delayedIterations:
        x.append(x[i - 1] + h * (a * x[i - 1] + u[i - 1 - delayedIterations]))
    else:
        x.append(x[i - 1] + h * (a * x[i - 1] + u[i - 1]))
    error.append(xSet - x[i])
    t.append(t[i - 1] + h)
    if i > int(T / h) / 2:
        xSet = 200
        if i > int(T / h) * 0.7:
            xSet = 150
    xSetLine.append(xSet)
print("Lowest unfitness: "+str(lowestUnfitness))
print(lowestUnfitnessGenome)
print(oldGenomes[0])
print(oldGenomes[1])
print(oldGenomes[2])
print(oldGenomes[3])
print(oldGenomes[4])
print(oldGenomes[5])
print(oldGenomes[6])
print(oldGenomes[7])
print(oldGenomes[8])
print(oldGenomes[9])
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
