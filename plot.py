import numpy as np
import matplotlib.pyplot as plt

with open('file.txt') as f:
    lines = f.readlines()
    x = [int(line.split()[0]) for line in lines]
    y = [int(line.split()[1]) for line in lines]

t = np.arange(13)

plt.scatter(x, y, c=t)
plt.show()