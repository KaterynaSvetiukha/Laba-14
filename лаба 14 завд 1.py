import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 10, 101)
y = np.cos(x**2) / x
plt.plot(x, y, label = 'cos(x) / x', color = 'purple', linewidth = 4)
plt.title('Task 1', fontsize=15, color='purple')

plt.xlabel('x', fontsize=12, color='red')
plt.ylabel('y', fontsize=12, color='red')
plt.legend()
plt.grid(True)
plt.show()