#Stratergy 1:
#Guess some numbers
import numpy as np
x_values = np.linspace(0,1,10000)

from pylab import *
def f(x):
    #return 5*log(x**3+2)-6+x
    return 350 * 1.2**x - 756

#check if the funtion is zero at the values
#for x in x_values:
   # if f(x) == 0:
       # print(x)

#Stratergy 2:        
#Guess a bunch of number, and check if they are close enough

precision = 0.001

#check if the funtion is zero at the values
#for x in x_values:
    #if abs(f(x)) < precision:
        #print(x)

#Strategy 3:
#Find where the sign of the function changes

#find where it swithes
#for i in range(0, len(x_values)-1):
    #a = x_values[i]
    #b = x_values[i+1]
    #if f(a)*f(b) < 0: #if one value is negative and one positiv, the anwser will become negative
        #midpoint = (a+b)/2
        #print(midpoint)

#Strategy 4 Halveringsmetoden
a = 0
b = 100
m = (a+b)/2

while abs(f(m)) > precision: #loops 
    if f(a)*f(m) < 0:
        b = m
    else:
        a = m
    m = (a+b)/2
    print(a, b)
print("The zero is about x=", m)