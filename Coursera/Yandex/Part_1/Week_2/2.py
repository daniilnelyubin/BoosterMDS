import numpy as np
import scipy.linalg
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x / 5) * np.exp(x / 10) + 5 * np.exp(-x / 2)

A = np.array([[1,1,1,1], [1,4,16,64],[1,10,100,1000],[1,15,225,3375]])
b = np.array([1,4,10,15])
b = f(b)
print(b)

print(scipy.linalg.solve(A,b))

# plt.plot(np.linspace)
plt.show()