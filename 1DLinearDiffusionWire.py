import numpy                 #loading our favorite library
from matplotlib import pyplot    #and the useful plotting library

nx = 41
dx = 2 / (nx - 1)
nt = 10000   #the number of timesteps we want to calculate
nu = 0.3   #the value of viscosity
sigma = .2 #sigma is a parameter, we'll learn more about it later
dt = sigma * dx**2 / nu #dt is defined using sigma ... more later!


u = numpy.zeros(nx)      #a numpy array with nx elements all equal to 1.

un = numpy.zeros(nx) #our placeholder array, un, to advance the solution in time

for n in range(nt):  #iterate through time
    un = u.copy() ##copy the existing values of u into un
    u[0]=3
    un[20]=5
    u[-1]=3
    u[20]=5
    for i in range(1, nx - 1):
        u[i] = un[i] + nu * dt / dx**2 * (un[i+1] - (2 * un[i]) + un[i-1])
    pyplot.ylim(top=5)  # adjust the top leaving bottom unchanged
    pyplot.ylim(bottom=0)
    pyplot.plot(numpy.linspace(0, 2, nx), u) ##Plot the results
    pyplot.draw()
    pyplot.pause(0.05)
    pyplot.clf()
    print(u)

# pyplot.ylim(top=5)  # adjust the top leaving bottom unchanged
# pyplot.ylim(bottom=0)
# pyplot.plot(numpy.linspace(0, 2, nx), u) ##Plot the results
# pyplot.draw()
# pyplot.pause(30)