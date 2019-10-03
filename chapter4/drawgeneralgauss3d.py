import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_range0 = [-3,3]
x_range1 = [-3,3]

def gauss(x,mu,sigma):
    N,D = x.shape
    c1 = 1 / (2 * np.pi)**(D / 2)    # a (height)
    c2 = 1 / (np.linalg.det(sigma)**(1 / 2))    # |sigma| ^1/2 ,
                                                # |sigma| = a1*a4-a2*a3
    inv_sigma = np.linalg.inv(sigma)
    c3 = x - mu
    c4 = np.dot(c3,inv_sigma)    # [x-mu] * [sigma]^-1
    c5 = np.zeros(N)

    for d in range(D):
        c5 = c5 + c4[:,d] * c3[:,d]    # 0 + [x-mu] * [sigma]^-1 * [x-mu]

    print(c3)
    print(c4)
    print(c5)
    
    p = c1 * c2 * np.exp(-c5 / 2)
    return p

def show_contour_gauss(mu,sig):
    xn = 40
    x0 = np.linspace(x_range0[0],x_range0[1],xn)
    x1 = np.linspace(x_range1[0],x_range1[1],xn)
    xx0,xx1 = np.meshgrid(x0,x1)

    x = np.c_[np.reshape(xx0,xn*xn,1),np.reshape(xx1,xn*xn,1)]
    f = gauss(x,mu,sig)
    f = f.reshape(xn,xn)
    f = f.T
    cont = plt.contour(xx0,xx1,f,15,colors="k")
    plt.grid(True)

def show3d_gauss(ax,mu,sig):
    xn = 40
    x0 = np.linspace(x_range0[0],x_range0[1],xn)
    x1 = np.linspace(x_range1[0],x_range1[1],xn)
    xx0,xx1 = np.meshgrid(x0,x1)

    x = np.c_[np.reshape(xx0,xn*xn,1),np.reshape(xx1,xn*xn,1)]
    f = gauss(x,mu,sig)
    f = f.reshape(xn,xn)
    f = f.T
    ax.plot_surface(xx0,xx1,f,rstride=2,cstride=2,alpha=0.3,
                    color="blue",edgecolor="black")

def main():
        
    mu = np.array([1,0.5])
    sigma = np.array([[2,1],[1,1]])

    Fig = plt.figure(1,figsize=(7,3))
    Fig.add_subplot(1,2,1)

    show_contour_gauss(mu,sigma)
    plt.xlim(x_range0)
    plt.ylim(x_range1)
    plt.xlabel("$x_0$",fontsize=18)
    plt.ylabel("$x_1$",fontsize=18)

    ax = Fig.add_subplot(1,2,2,projection="3d")
    show3d_gauss(ax,mu,sigma)

    ax.set_zticks([0.05,0.10])
    ax.set_xlabel("$x_0$",fontsize=18)
    ax.set_ylabel("$x_1$",fontsize=18)
    ax.set_zlabel("$y$",fontsize=18)
    ax.view_init(40,-125)

    plt.show()

if __name__ == "__main__":
    main()
