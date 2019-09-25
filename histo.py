# 25 Sept 2019
# 52465 Programming for Data Analysis 
# Lecture 2
import matplotlib.pyplot as plt
import numpy as np

plt.subplot(1, 2, 1)
x = np.random.normal(0.0, 1.0, 10000)
plt.hist(x)
plt.xlabel('x')
plt.ylabel('Normal distribution')

plt.subplot(1, 2, 2)
x = np.random.uniform(-3.0, 3.0, 10000)
plt.hist(x)
plt.xlabel('x')
plt.ylabel('Uniform distribution')


plt.show()