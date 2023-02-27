#Q1
#10 Mark


import math as m
from sympy import var
from sympy import sympify
 
def simpsons_1by3( lower_limit, upper_limit, n ,f): 
    h = ( upper_limit - lower_limit )/n
    xb = list()
    fx = list()
    i = 0
    while i<= n:
        xb.append(lower_limit + i * h)
        fx.append(f.subs(x,xb[i]))
        i += 1
    res = 0
    i = 0
    while i<= n:
        if i == 0 or i == n:
            res+= fx[i]
        elif i % 2 != 0:
            res+= 4 * fx[i]
        else:
            res+= 2 * fx[i]
        i+= 1
    res = res * (h / 3)
    return res

def simpsons_3by8(lower_limit, upper_limit, interval_limit,f ):    
    h = (float(upper_limit - lower_limit) / interval_limit)
    sum = f.subs(x,lower_limit) + f.subs(x,upper_limit)
    for i in range(1, interval_limit ):
        if (i % 3 == 0):
            sum = sum + 2 * f.subs(x,lower_limit + i * h)
        else:
            sum = sum + 3 * f.subs(x,lower_limit + i * h)
     
    return ((float( 3 * h) / 8 ) * sum )     

def trapezoidal(lower_limit,upper_limit,n,f):
    h = (upper_limit - lower_limit) / n
    
    integration = f.subs(x,lower_limit) + f.subs(x,upper_limit)
    
    for i in range(1,n):
        k = lower_limit + i*h
        integration = integration + 2 * f.subs(x,k)
    
    integration = integration * h/2
    
    return integration


eq = input("Enter equation f(x):")
lower_limit = float(input("Enter the lower limit : "))
upper_limit = float(input("Enter the upper limit : "))

x = var('x')
f = sympify(eq)

n = 6 
#f = lambda x :eval(eq)
print(f)
print("The value of the given integral using Simpsion's 1/3 rule : ",simpsons_1by3(lower_limit, upper_limit, n,f))
print("The value of the given integral using Simpsion's 3/8 rule : ",simpsons_3by8(lower_limit, upper_limit, n,f))
print("The value of the given integral using trapezoidal rule : ",trapezoidal(lower_limit, upper_limit, n,f))




#5 MARK

#NEWTONS FORWARD

import math, sys

# -----------------------------------------------------------------------------

x = []
n = int(input("Enter the order n : "))
y = [[0 for i in range(n)] for j in range(n)]

# -----------------------------------------------------------------------------

for i in range(n):
    x.append(float(input("Enter the values of x" + str(i) + " : " )))

for i in range(n):
    y[i][0] = float(input("Enter the values of y" + str(i) + " : "))

# -----------------------------------------------------------------------------

pt = float(input("Enter the point of interpolation : "))

# checkin for equally spaced
space = abs(x[1] - x[0])

for i in range(0, len(x) - 1):
    
    if(abs(x[i] - x[i+1]) != space):
        print("Not Equally Spaced ! Will not be able to calculate value !")
        sys.exit()

# -----------------------------------------------------------------------------
# Calculating the forward difference
# -----------------------------------------------------------------------------

for i in range(1, n):
    for j in range(n - i):
        y[j][i] = y[j+1][i-1] - y[j][i-1]

for i in range(n):
    for j in range(n-i):
        print(y[i][j], end = "\t")
    print()

# -----------------------------------------------------------------------------

res = y[0][0]
u = (pt - x[0]) / (x[1] - x[0])

# -----------------------------------------------------------------------------

for i in range(1,n):
    temp = u
    for j in range(1,i):
        temp *= (u - j)
    res = res + (temp * y[0][i]) / math.factorial(i)
    
# -----------------------------------------------------------------------------

print("The interpolated value at %0.0f is %0.2f" %(pt,res))

# -----------------------------------------------------------------------------



#NEWTONS BACKWARD

import math, sys

# -----------------------------------------------------------------------------

x = []
n = int(input("Enter the order n :"))
y = [[0.0 for i in range(n)] for j in range(n)]

# -----------------------------------------------------------------------------

for i in range(n):
    x.append(float(input("Enter the values of x" + str(i) + " : " )))

for i in range(n):
    y[i][0] = float(input("Enter the values of y" + str(i) + " : "))

# -----------------------------------------------------------------------------

pt = float(input("Enter the point of interpolation : "))

# checkin for equally spaced
space = abs(x[1] - x[0])

for i in range(0, len(x) - 1):
    
    if(abs(x[i] - x[i+1]) != space):
        print("Not Equally Spaced ! Will not be able to calculate value !")
        sys.exit()

# -----------------------------------------------------------------------------
# Calculating the forward difference
# -----------------------------------------------------------------------------

for i in range(1,n):
    for j in range(n-1, i-1, -1):
        y[j][i] = y[j][i-1] - y[j-1][i-1]

for i in range(n):
    for j in range(i + 1):
        print(y[i][j], end = "\t")
    print()

# -----------------------------------------------------------------------------

res = y[n - 1][0]
u = (pt - x[n - 1]) / (x[1] - x[0])

# -----------------------------------------------------------------------------

for i in range(1, n):
    temp = u
    for j in range(i):
        temp = temp * (u + j)
    res = res + (temp * y[n-1][i]) / math.factorial(i)

# -----------------------------------------------------------------------------

print("The interpolated value at %0.0f is %0.2f" %(pt, res))

# -----------------------------------------------------------------------------



##Second 10 mark
# Divided difference, lagrange, inverse lagrange, cubic spline


#DIVIDED DIFFERENCE
import math

def proterm(i, value, x):
    
    pro = 1
    for j in range(i):
        pro = pro * (value - x[j])
    return pro
 
def dividedDiffTable(x, y, n):
    
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1])/(x[j] - x[i + j]))
    return y

def applyFormula(value, x, y, n):
    
    sum = y[0][0]
    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i])     
    return sum
 
def printDiffTable(y, n):
    
    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 4), "\t", end = " ")
        print("")

i = 0
n = 0
x = [] 

n = int(input("\nEnter the number of Variables : "))

print("Enter the Values : ")
for i in range(0, n):
    
    dummy = float(input())
    x.append(dummy)

y = [[0 for i in range(n+1)] for j in range(n)]
    
print("Enter the f(x) values respetively : ")
for i in range(0, n):

    dummy = float(input())
    y[i][0] = dummy

#choice = input("Is the value to find for in exponential ? If yes Press Y/y else Press N/n ")
value = float(input("Enter the value to find for : "))

# to check for exp input
"""
if choice == 'Y' or choice =='y':
    value = float(input("Enter the power of the exponent : "))
    value = math.exp(value)
elif choice == 'N' or choice =='n':
    value = float(input("Enter the value to find for : "))
"""
y = dividedDiffTable(x, y, n)

print("\nDivided Difference Table : \n")
printDiffTable(y, n)
 
print("\nValue at", value, "is", round(applyFormula(value, x, y, n), 4))



#LAGRANGE
import sympy as sp

# -----------------------------------------------------------------------------

a = []
y = []

# -----------------------------------------------------------------------------

n = int(input("Enter the order n : "))

# -----------------------------------------------------------------------------

for i in range(n):
    temp = float(input("Enter the values of x" + str(i) + " : " ))
    a.append(temp)
    temp = float(input("Enter the values of f(x" + str(i) + ") : "))
    y.append(temp)

# -----------------------------------------------------------------------------

yp = 0
pt = float(input("Enter the value of x to substitute : "))
x  = sp.Symbol('x')

for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (x - a[j])/(a[i] - a[j])
    
    yp = yp + p * y[i] 

print("the interpolated expression is :", yp)
print("The interpolated value is :", round(yp.subs(x, pt), 4))

# -----------------------------------------------------------------------------



#INVERSE LEGRANGE
a = []
y = []

n = int(input("Enter the order n : "))

# -----------------------------------------------------------------------------

for i in range(n):
    
    temp = float(input("Enter the values of x" + str(i) + " : " ))
    a.append(temp)
    temp = float(input("Enter the values of f(x" + str(i) + ") : "))
    y.append(temp)

# -----------------------------------------------------------------------------

yp = 0
pt = float(input("Enter the value of x to substitute:"))

# -----------------------------------------------------------------------------

for i in range(n):
    p = 1
    for j in range(n):
        if i != j:
            p = p * (pt - y[j]) / (y[i] - y[j])
    yp = yp + p * a[i] 
    
# -----------------------------------------------------------------------------

print("\nThe value of x is :", round(yp, 4))

# -----------------------------------------------------------------------------




#CUBIC SPLINE

import numpy as np
import sympy as sp

# -----------------------------------------------------------------------------

def ch(n):
  if n < 0:
    return '-'
  else:
    return '+'

# -----------------------------------------------------------------------------

n = int(input("Enter number of values : "))
x  = []
fx = []

for i in range(n):
  x.append(float(input("Enter x : ")))
  fx.append(float(input("Enter f(x) : ")))

'''n=4
x=[1,2,3,4]
fx=[1,5,11,8]'''

# -----------------------------------------------------------------------------

h = x[1] - x[0]
d = []

# -----------------------------------------------------------------------------

for i in range(1, n - 1):
  d.append(6 * (fx[i-1] - 2 * fx[i] + fx[i+1]) / (h*h) )
  
# -----------------------------------------------------------------------------

a = np.zeros((n-2, n-2))

for i in range(n - 2):
  for j in range(n - 2):
    
    if i == j:
      a[i][j] = 4
      
    elif abs(i-j) == 1:
      a[i][j] = 1

m = np.linalg.solve( a, np.array(d) )
m = m.tolist()
m.insert(0, 0)
m.insert(n, 0)

px = []

# -----------------------------------------------------------------------------

print("\nThe Cubic Equations : \n")
for i in range(n - 1):
  t = "%f*(%f - x)**3/6*%d %c %f*(x %c %f)**3/6*%d + (%f - x)*(%f %c %f*%d/6)/%d + (x %c %f)*(%f %c %f*%d/6)/%d"%(m[i],x[i+1],h,ch(m[i+1]),abs(m[i+1]),ch(-x[i]),abs(x[i]),h,x[i+1],fx[i],ch(-m[i]),abs(m[i]),h*h,h,ch(-x[i]),abs(x[i]),fx[i+1],ch(-m[i+1]),abs(m[i+1]),h*h,h)
  px.append(str(sp.expand(t)))
  print("p%d(x) = %s"%((i+1),px[i]))

X = float(input("\nEnter the x to find f(x) :"))

for i in range(len(x)):
  if x[i] >= X:
    break

print("\nf(%.2f) = %.2f"%(X,eval((px[i-1]).replace('x',str(X)))))

# -----------------------------------------------------------------------------

