import numpy as np
import matplotlib.pyplot as plt

def main():

    x = np.linspace(-8,8,100)
    y = 2**x
    
    x2 = np.linspace(0.001,8,100)
    y2 = np.log(x2) / np.log(2)

    plt.figure(figsize=(5,5))
    plt.plot(x,y, "black",linewidth=2, label="$y=2^x$")
    plt.plot(x2,y2,"cornflowerblue",linewidth=2, label="$y=\log_{2}x$")
    plt.plot(x,x,"gray",linestyle="--",linewidth=2, label="$y=x$")

    plt.ylim(-8,8)
    plt.xlim(-8,8)

    plt.grid(True)
    plt.legend(loc="upper left")
    plt.show()

if __name__ == "__main__":
    main()
