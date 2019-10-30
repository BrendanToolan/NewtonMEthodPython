#adpated from https://tour.golang.org/flowcontrol/8

def sqrt(x):
    #inital guess
    z = 1.0
    # keep getting better estimamte for sq root 
    # of x until within two decimal places.

    while abs(z*z -x) >= 0.01:
        #get better approxication for sq root
        z -= (z*z -x) / (2*z)
    #return z
    return z

sqrt(8.0)

