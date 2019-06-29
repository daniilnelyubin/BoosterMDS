import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from scipy.optimize import differential_evolution
from math import *
def f(x):
    return int(sin(x / 5) * exp(x / 10) + 5 * exp(-x / 2))

# x = np.linspace(1,30,100)
# plt.plot(x,f(x))
# plt.show()


min_1 = minimize(f,x0=30,method="BFGS",tol=1e-2)
print(f(min_1.x))

min_2 = differential_evolution(f,bounds=[(1,30)],tol=1e-2)
print(f(min_2.x))





