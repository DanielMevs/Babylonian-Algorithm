import math
def bab(x):
    
    x0 = 0.1
    x1 = x/2
    if(x<0):
        raise Exception("x should not be less than 0. The value of x was: ", x)
    while .01 <= abs(x1-x0)/x0:
        x0 = x1
        r = x/x0
        x1 = (x0+r)/2
    print(x1)
    return x1

x = 0
x = float(input("Please input the value of x: "))
bab_sqrt = bab(x)
print("The the square root of ", x," as approximated by by the Babylonian algorithm is: ", bab_sqrt)
print("The the square root of ", x," as approximated by by the math module is: ", math.sqrt(x))


    
    
