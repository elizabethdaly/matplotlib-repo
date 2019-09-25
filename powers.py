# 25 Sept 2019
# 52465 Programming for Data Analysis 
# Lecture 2
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1.0, 10.0, 0.1)

plt.plot(x, x**2, 'g-', label='x^2')
plt.plot(x, x**3, 'b-', label='x^3')
plt.plot(x, x**4, 'r-', label='x^4')
plt.plot(x, 2**x, 'g-', label='2^x')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
