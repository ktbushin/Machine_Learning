import numpy as np
import matplotlib.pyplot as plt

def f2(x,w):
    return (x-w) * x * (x+2)

x = np.linspace(-3,3,100)        #100等分

plt.figure(figsize=(10,4))        #全体の広さ inch * inch
plt.subplots_adjust(wspace=0.5, hspace=0.5)    #グラフの間隔

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.title("$f(x)=(x-{0})*x*(x+2)$" .format(i))
    plt.plot(x,f2(x,i))
    plt.ylim(-20,20)
    plt.grid(True)


plt.show()
