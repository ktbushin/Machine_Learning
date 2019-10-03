import numpy as np
import matplotlib.pyplot as plt

def f3(x0,x1):
    ans = (2 * x0**2 + x1**2) * np.exp(-(2 * x0**2 + x1**2))
    return ans

def set_array(xn,x0,x1):
    y = np.zeros((len(x0),len(x1)))
    

    for i0 in range(xn):
        for i1 in range(xn):
            y[i1,i0] = f3(x0[i0],x1[i1])    #あえて対称に入れる

    return y



def main():

    xn = 9
    x0 = np.linspace(-2,2,xn)
    x1 = np.linspace(-2,2,xn)

    y = set_array(xn,x0,x1)
       
    print(np.round(y,2))
   

if __name__ == "__main__":
    main()
