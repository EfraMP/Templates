import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

x = np.linspace(0,10,1000)

goals = [2, 3, 4, 5]

for i in goals:
    plt.plot(x, gamma.pdf(x, a = i, scale = 1), label=f'alpha={i}')
plt.legend()
plt.title("Probabilidades a priori")
plt.xlabel('X')
plt.ylabel('PDF')
plt.grid(alpha=0.3)
plt.savefig('others.png', dpi=300) 
plt.show()