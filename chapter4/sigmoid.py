import numpy as np
import matplotlib.pyplot as plt

def main():

    x = np.linspace(-10,10,100)
    y = 1 / (1 + np.exp(-x))
    dy = y*(1-y)

    
    plt.figure(figsize=(5,5))
    plt.plot(x,y, "black",linewidth=2, label="$y = 1 / (1 + e^{-x})$")
    plt.plot(x,dy,"cornflowerblue",linewidth=2,linestyle="--",
             label="$dy/dx = y(1-y)$")

    plt.ylim(-1,2)
    plt.xlim(-10,10)

    plt.grid(True)
    plt.legend(loc="upper left")
    plt.show()

if __name__ == "__main__":
    main()
