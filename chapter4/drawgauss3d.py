import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def gauss(x0,x1):
    
    return np.exp(-1*(x0**2 + x1**2))


def main():
    
    xn = 50
    x0 = np.linspace(-4,4,xn)
    x1 = np.linspace(-4,4,xn)
    
    y = np.zeros((xn,xn,3))
    for i0 in range(xn):
        for i1 in range(xn):
            y[i1,i0] = gauss(x0[i0],x1[i1])

    xx0,xx1 = np.meshgrid(x0,x1)

    plt.figure(figsize=(5,5))

    ax = plt.subplot(1,1,1,projection="3d")
    ax.plot_surface(xx0,xx1,y[:,:,0],
                    rstride=1, cstride=1,
                    alpha=0.5, color="blue",edgecolor="black")
    
    ax.set_xlabel("$x_0$",fontsize=18)
    ax.set_ylabel("$x_1$",fontsize=18)
    ax.set_zlabel("$y$",fontsize=18)
    ax.view_init(40,-125)

    plt.show()

if __name__ == "__main__":
    main()
