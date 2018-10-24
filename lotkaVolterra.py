import matplotlib.pyplot as plt
import math


# Rabbit equation
def fR(x, y):
    return ((a*x) - (b*x*y))


# Foxes equation
def fF(x, y):
    return ((-c)*y + (d*x*y))


def rungeKutta(x0, y0, h, iters):
    # Add the initial values to the lists
    # Time list
    t = [0]
    # Rabbit population list
    r = [x0]
    # Foxes population list
    f = [y0]

    for i in range(0, iters):
        # Increment h to time and add it to the time list
        t.append(t[i] + h)
        # k1 calculation
        k1R = fR(r[i], f[i])
        k1F = fF(r[i], f[i])
        # k2 calculation
        k2R = fR(r[i] + h/2.0 * k1R, f[i] + h/2.0 * k1F)
        k2F = fF(r[i] + h/2.0 * k1R, f[i] + h/2.0 * k1F)
        # k3 calculation
        k3R = fR(r[i] + h/2.0 * k2R, f[i] + h/2.0 * k2F)
        k3F = fF(r[i] + h/2.0 * k2R, f[i] + h/2.0 * k2F)
        # k4 calculation
        k4R = fR(r[i] + h*k3R, f[i] + h*k3F)
        k4F = fF(r[i] + h*k3R, f[i] + h*k3F)
        # Add result to rabbits ammount of population list
        r.append(r[i] + (h/6.0) * (k1R + 2*k2R + 2*k3R + k4R))
        # Add result to foxes ammount of population list
        f.append(f[i] + (h/6.0) * (k1F + 2*k2F + 2*k3F + k4F))
    return t, r, f


def plotPredandPrey(t, r, f):
    plt.grid()

    plt.plot(t, f, 'C1', label='Zorros')
    plt.plot(t, r, 'C5', label='Conejos')
    plt.xlabel("Tiempo")
    plt.ylabel("Poblacion")
    axes = plt.gca()
    # X axis range
    axes.set_xlim([0, 200])
    # Y axis range
    axes.set_ylim([0, 56])

    plt.legend()
    plt.show()


def plotPredvsPrey(r, f):
    plt.grid()
    plt.plot(r, f, 'C3')
    plt.xlabel("Poblacion de conejos")
    plt.ylabel("Poblacion de zorros")

    plt.show()


if __name__ == '__main__':
    # Parameters
    a = 0.1
    b = 0.02
    c = 0.3
    d = 0.01

    # Initial rabbit population
    x0 = 40
    # Initial foxes population
    y0 = 9

    # Step for numerical approximation
    h = 0.05

    # Final time
    tfinal = 200

    # Number of iterations for the approximation
    iters = tfinal/h

    t, r, f = rungeKutta(x0, y0, h, int(iters))

    # Print in console the result in format: Time - RabbitPopulation - FoxesPopulation
    for i, j, k in zip(t, r, f):
        print(str(i) + " - " + str(j) + " - " + str(k))

    axes = plt.gca()

    # Plot the predator and prey population through time
    plotPredandPrey(t, r, f) 

    # Plot the predator vs prey population
    plotPredvsPrey(r, f)
