import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():

    np.random.seed(seed=1)
    x_min = 4
    x_max = 30
    x_n = 16
    x = 5 + 25 *np.random.rand(x_n)
    prm_c = [170,108,0.2]
    t = prm_c[0] - prm_c[1] * np.exp(-prm_c[2] * x) \
        + 4 * np.random.rand(x_n)

    print(np.round(x,2))
    print(np.round(t,2))

    #np.savez("ch_5data.npz",x=x,x_min=x_min,x_max=x_max,x_n=x_n,t=t)

    plt.figure(figsize=(4,4))
    plt.plot(x,t,marker="o",linestyle="None",
             markeredgecolor="black",color="cornflowerblue")
    plt.xlim(x_min,x_max)
    plt.grid(True)
    plt.show()
    
if __name__ == "__main__":
    main()

