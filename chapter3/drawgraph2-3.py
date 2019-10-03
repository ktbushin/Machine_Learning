import numpy as np
import matplotlib.pyplot as plt
import drawgraph2_1 as one
from mpl_toolkits.mplot3d import Axes3D

def main():
    xn = 50
    x0 = np.linspace(-2,2,xn)
    x1 = np.linspace(-2,2,xn)

    y = one.set_array(xn,x0,x1)

    xx0,xx1 = np.meshgrid(x0,x1)


    plt.figure(figsize = (10,10))

    ax = plt.subplot(1,1,1,projection="3d")
    ax.plot_surface(xx0, xx1, y, rstride = 1, cstride = 1,
                    alpha=0.5, color="blue", edgecolor = "black")

    ax.set_zticks((0,0.2))

    ax.view_init(75,-95)

    plt.show()
    
if __name__ == "__main__":
    main()
