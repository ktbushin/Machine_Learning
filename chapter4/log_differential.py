import numpy as np
import matplotlib.pyplot as plt

def main():

    x = np.linspace(0.0001,4,100)
    y = np.log(x)
    dy = 1/x

    
    plt.figure(figsize=(5,5))
    plt.plot(x,y, "black",linewidth=2, label="$y = log{x}$")
    plt.plot(x,dy,"cornflowerblue",linewidth=2,
             label="$dy/dx = 1 / x$")

    plt.ylim(-8,8)
    plt.xlim(-1,4)

    plt.grid(True)
    plt.legend(loc="upper left")
    plt.show()

if __name__ == "__main__":
    main()
