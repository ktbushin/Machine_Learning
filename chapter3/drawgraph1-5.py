import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (x-2) * x * (x+2)

x = np.arange(-5,5,0.5)
y = f(x)

print("x = ",end = " [")
print(*x,sep = "    ",end = "")        #x unpack
print("  ]")

print("y = ",end = " ")
print(np.round(y,2))


plt.plot(x,y)
plt.show()
