import numpy                 # we're importing numpy 
from matplotlib import pyplot    # and our 2D plotting library


nx = 41
dx = 2 / (nx - 1)
nt = 250   #nt is the number of timesteps we want to calculate
dt = .025  #dt is the amount of time each timestep covers (delta t)
c = 1

u = numpy.zeros(nx)      #as before, we initialize u with every value equal to 1.
u[int(.5 / dx) : int(.75 / dx + 1)] = 2
u[int(.75 / dx) : int(1 / dx + 1)] = 1

un = numpy.ones(nx) #initialize our placeholder array un, to hold the time-stepped solution
# pyplot.ylim([0, 2])    
# pyplot.plot(numpy.linspace(0, 2, nx), u) ##Plot the results
# pyplot.draw()
# pyplot.pause(10)
# pyplot.clf()
for n in range(nt):  #iterate through time
    un = u.copy() ##copy the existing values of u into un
    for i in range(1, nx):  ##now we'll iterate through the u array
    
     ###This is the line from Step 1, copied exactly.  Edit it for our new equation.
     ###then uncomment it and run the cell to evaluate Step 2   
      
        u[i] = un[i] - (c * (dt / dx) * (un[i] - un[i-1]))
    u[0] = u[-1]
    pyplot.ylim([0, 2])    
    pyplot.plot(numpy.linspace(0, 2, nx), u) ##Plot the results
    pyplot.draw()
    pyplot.pause(.001)
    pyplot.clf()