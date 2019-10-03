import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(seed=1)
x_min = 4
x_max = 30
x_n = 16
x = 5 + 25 *np.random.rand(x_n)
prm_c = [170,108,0.2]
t = prm_c[0] - prm_c[1] * np.exp(-prm_c[2] * x) + 4 * np.random.rand(x_n)


def mse_line(x,t,w):    # mean squared error
    y = w[0] * x + w[1]
    mse = np.mean((y-t)**2)
    return mse

def main():
    
    xn = 100
    w0_range = [-25,25]
    w1_range = [120,170]

    w0 = np.linspace(w0_range[0],w0_range[1],xn)
    w1 = np.linspace(w1_range[0],w1_range[1],xn)
    ww0, ww1 = np.meshgrid(w0,w1)

    J = np.zeros((len(w0),len(w1)))

    for i0 in range(len(w0)):
        for i1 in range(len(w1)):
            J[i1,i0] = mse_line(x,t,(w0[i0],w1[i1]))
    
    
    plt.figure(figsize=(10,4))
    plt.subplots_adjust(wspace =0.5)

    ax = plt.subplot(1,2,1,projection="3d")
    ax.plot_surface(ww0,ww1,J,rstride=10,cstride=10,alpha=0.3,
                    color="blue",edgecolor="black")
    ax.set_xticks([-20,0,20])
    ax.set_yticks([120,140,160])
    ax.set_xlabel("$w_0$")
    ax.set_ylabel("$w_1$")
    ax.view_init(20,-60)

    plt.subplot(1,2,2)
    cont = plt.contour(ww0,ww1,J,30,colors="blue",
                       levels=[100,1000,10000,100000])
    cont.clabel(fmt="%d",fontsize=10)
    plt.xlabel("$w_0$")
    plt.ylabel("$w_1$")
    plt.xlim(-10,10)
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    main()
