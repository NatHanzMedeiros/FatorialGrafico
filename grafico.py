import matplotlib.pyplot as plt
import math

x = range(0, 6)
y = [math.factorial(n) for n in x]

plt.plot(x, y, marker='o')
plt.xlabel('Número')
plt.ylabel('Fatorial')
plt.title('Crescimento dos Números Fatoriais')
plt.grid(True)
plt.show()
