import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)
x = np.arange(10)
y = np.random.random((10))

print("x = ",end = " [")
print(*x,sep = "    ",end = "")        #x unpack
print("  ]")

print("y = ",end = " ")
print(np.round(y,2))


plt.plot(x,y)
plt.show()

