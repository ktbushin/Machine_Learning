import numpy as np
import matplotlib.pyplot as plt

def softmax(x0,x1,x2):
    u = np.exp(x0) + np.exp(x1) + np.exp(x2)
    return np.exp(x0)/u, np.exp(x1)/u, np.exp(x2)/u


def main():

    y = softmax(2,1,-1)
    print(np.round(y,4))
    print(np.sum(y))


if __name__ == "__main__":
    main()
