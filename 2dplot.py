# 25 Sept 2019
# 52465 Programming for Data Analysis 
# Lecture 2
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0
noise = np.random.normal(0.0, 1.0, len(x))

plt.plot(x, y + noise, 'r.', label='Actual')
plt.plot(x, y, 'b-', label='Model')

plt.title('Simple plot')
plt.xlabel('x values')
plt.ylabel('y values')
plt.legend()
plt.show()

""" Simple plotting video
# plt.plot([1, 2, 3, 4])  straight line
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'b.') # list2 vs list1 scatterplot
plt.ylabel("Some numbers")
plt.show() """