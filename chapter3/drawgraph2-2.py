import numpy as np
import matplotlib.pyplot as plt
import drawgraph2_1 as one

def main():
    xn = 200
    x0 = np.linspace(-2,2,xn)
    x1 = np.linspace(-2,2,xn)

    y = one.set_array(xn,x0,x1)


    plt.figure(figsize = (10,10))
    #plt.jet()
    plt.gray()
    #plt.pink()
    #plt.bone()
    plt.pcolor(y)
    plt.colorbar()
    plt.show()


if __name__ == "__main__":
    main()


