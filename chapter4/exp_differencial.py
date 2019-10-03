import numpy as np
import matplotlib.pyplot as plt

def main():

    x = np.linspace(-4,4,100)
    a = 2
    y = a**x
    dy = np.log(a) * y

    
    plt.figure(figsize=(5,5))
    plt.plot(x,y, "black",linewidth=2, label="$y = 2^x$")
    plt.plot(x,dy,"cornflowerblue",linewidth=2,
             label="$dy/dx= 2^x * \log{2}$")

    plt.ylim(-1,8)
    plt.xlim(-4,4)

    plt.grid(True)
    plt.legend(loc="upper left")
    plt.show()

if __name__ == "__main__":
    main()
