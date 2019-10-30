#adpated from https://tour.golang.org/flowcontrol/8

def sqrt(x):
    #inital guess
    z = 1.0
    # keep getting better estimamte for sq root 
    # of x until within two decimal places.
    while abs(z*z - x) >= 0.0001:
        #get better approxication for sq root
        z -= (z*z -x) / (2*z)
    #return z
    return z

#calculate sq root of 8
z = sqrt(100001.0)
#print z 
print(z)
#print(sqrt(8.0))
#print sq of the sq root
print(z*z)
