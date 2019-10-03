import numpy as np
import matplotlib.pyplot as plt

def gauss(x,mu,sigma,a):
    return a * np.exp(-(x-mu)**2 / (2 * sigma**2))

def main():

    x = np.linspace(-4,4,100)
    print(type(x))
    print(np.round(x,3))

    plt.figure(figsize=(5,5))
    plt.plot(x,gauss(x,0,1,1),  "black",linewidth=2, label="$y = exp(-x^2 / 2*1^2)$")
    plt.plot(x,gauss(x,2,2,0.5),"cornflowerblue",linewidth=2,
             label="$y =  0.5*exp(-(x-2)^2 / 2*2^2)$")

    plt.xlim(-4,4)
    plt.ylim(-0.5,1.5)

    plt.grid(True)
    plt.legend(loc="upper left")
    plt.show()

if __name__ == "__main__":
    main()
