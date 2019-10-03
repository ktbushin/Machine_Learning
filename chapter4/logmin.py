import numpy as np
import matplotlib.pyplot as plt

def main():

    x = np.linspace(-4,4,100)
    y = (x-1)**2+2
    logy = np.log(y)

    
    plt.figure(figsize=(5,5))
    plt.plot(x,y, "black",linewidth=2, label="$y=(x-1)^2 + 2$")
    plt.plot(x,logy,"cornflowerblue",linewidth=2,
             label="$y=\log_e{(x-1)^2 + 2}$")

    plt.yticks(range(-4,9,1))
    plt.xticks(range(-4,5,1))
  
    plt.ylim(-4,8)
    plt.xlim(-4,4)

    plt.grid(True)
    plt.legend(loc="lower left")
    plt.show()

if __name__ == "__main__":
    main()
