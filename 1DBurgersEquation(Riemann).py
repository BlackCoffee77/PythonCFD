import numpy
import sympy
from matplotlib import pyplot
from sympy import init_printing
init_printing(use_latex=True)
from sympy.utilities.lambdify import lambdify


# x, nu, t = sympy.symbols('x nu t')
# phi = (sympy.exp(-(x - 4 * t)**2 / (4 * nu * (t + 1))) +
#        sympy.exp(-(x - 4 * t - 2 * sympy.pi)**2 / (4 * nu * (t + 1))))

# phiprime = phi.diff(x)

# u = -2 * nu * (phiprime / phi) + 4

# ufunc = lambdify((t, x, nu), u)
# print(ufunc(1, 4, 0))

nx = 101
nt = 10000000
nta = 0
dx = 2 * numpy.pi / (nx - 1)
nu = 0.000001
dt = dx * nu

x = numpy.linspace(0, 2 * numpy.pi, nx)
un = numpy.empty(nx)
t = 0

# u = numpy.asarray([ufunc(t, x0, nu) for x0 in x])

# u_analytical = numpy.asarray([ufunc(nta * dt, xi, nu) for xi in x])
u = numpy.ones(nx)
u[int(.5 / dx) : int(1 / dx + 1)] = 5
u_analytical=numpy.ones(nx)
u_analytical[int(.5 / dx) : int(1 / dx + 1)] = 5

pyplot.figure(figsize=(11, 7), dpi=100)
for n in range(nt):
    un = u.copy()
    for i in range(1, nx-1):
        u[i] = un[i] - un[i] * dt / dx *(un[i] - un[i-1]) + nu * dt / dx**2 * (un[i+1] - 2 * un[i] + un[i-1])
        
    u[0] = un[0] - un[0] * dt / dx * (un[0] - un[-2]) + nu * dt / dx**2 * (un[1] - 2 * un[0] + un[-2])
    u[-1] = u[0]
    
    pyplot.plot(x,u, marker='o', lw=2, label='Position: '+ str(n))
    print(u)
    pyplot.plot(x, u_analytical, label='Initial Condition')
    pyplot.ylim([0, 10])
    pyplot.legend()
    pyplot.draw()
    pyplot.pause(.001)
    pyplot.clf()