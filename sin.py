# 25 Sept 2019
# 52465 Programming for Data Analysis 
# Lecture 2
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2.0 * np.pi, 2.0 * np.pi, 0.1)

plt.plot(x, np.sin(x), 'g.', label='Sine')
plt.plot(x, np.cos(x), 'b.', label='Cosine')

plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.show()
