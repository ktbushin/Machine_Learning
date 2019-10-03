import numpy as np
import matplotlib.pyplot as plt

def f2(x,w):
    return (x-w) * x * (x+2)

def main():
    
    x = np.linspace(-3,3,100)        #100等分


    plt.plot(x,f2(x,2),color="black",label="$w=2$")
    plt.plot(x,f2(x,1),color="cornflowerblue",label="$w=1$")
    
    plt.legend(loc="upper left")
    plt.ylim(-15,15)
    plt.xlabel("$x axis$")
    plt.ylabel("$y axis$")
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    main()
