# Newton's divided difference, lagrange, inverse lagrange, cubic spline

# Newton divided difference formula
 
# Function to find the product term
def proterm(i, value, x):
    pro = 1;
    for j in range(i):
        pro = pro * (value - x[j]);
    return pro;
 
# Function for calculating
# divided difference table
def dividedDiffTable(x, y, n):
 
    for i in range(1, n):
        for j in range(n - i):
            y[j][i] = ((y[j][i - 1] - y[j + 1][i - 1]) /
                                     (x[j] - x[i + j]));
    return y;
 
# Function for applying Newton's
# divided difference formula
def applyFormula(value, x, y, n):
 
    sum = y[0][0];
 
    for i in range(1, n):
        sum = sum + (proterm(i, value, x) * y[0][i]);
     
    return sum;
 
# Function for displaying divided
# difference table
def printDiffTable(y, n):
 
    for i in range(n):
        for j in range(n - i):
            print(round(y[i][j], 4), "\t",
                               end = " ");
 
        print("");
 
# Driver Code
 
# number of inputs given
n = 4;
y = [[0 for i in range(10)]
        for j in range(10)];
x = [ 5, 6, 9, 11 ];
 
# y[][] is used for divided difference
# table where y[][0] is used for input
y[0][0] = 12;
y[1][0] = 13;
y[2][0] = 14;
y[3][0] = 16;
 
# calculating divided difference table
y=dividedDiffTable(x, y, n);
 
# displaying divided difference table
printDiffTable(y, n);
 
# value to be interpolated
value = 7;
 
# printing the value
print("\nValue at", value, "is",
        round(applyFormula(value, x, y, n), 2))


# of Lagrange's Interpolation
 
# To represent a data point corresponding to x and y = f(x)
class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
# function to interpolate the given data points
# using Lagrange's formula
# xi -> corresponds to the new data point
# whose value is to be obtained
# n -> represents the number of known data points
def interpolate(f: list, xi: int, n: int) -> float:
 
    # Initialize result
    result = 0.0
    for i in range(n):
 
        # Compute individual terms of above formula
        term = f[i].y
        for j in range(n):
            if j != i:
                term = term * (xi - f[j].x) / (f[i].x - f[j].x)
 
        # Add current term to result
        result += term
 
    return result
 
# Driver Code
if __name__ == "__main__":
 
    # creating an array of 4 known data points
    f = [Data(0, 2), Data(1, 3), Data(2, 12), Data(5, 147)]
 
    # Using the interpolate function to obtain a data point
    # corresponding to x=3
    print("Value of f(3) is :", interpolate(f, 3, 4))




# inverse interpolation

class Data:
    def __init__(self, x, y):
        self.x = x
        self.y = y
 
# Function to calculate
# the inverse interpolation
def inv_interpolate(d: list, n: int,
                    y: float) -> float:
 
    # Initialize final x
    x = 0
 
    for i in range(n):
 
        # Calculate each term
        # of the given formula
        xi = d[i].x
        for j in range(n):
            if j != i:
                xi = (xi * (y - d[j].y) /
                      (d[i].y - d[j].y))
 
        # Add term to final result
        x += xi
    return x
 
# Driver Code
if __name__ == "__main__":
 
    # Sample dataset of 4 points
    # Here we find the value
    # of x when y = 4.5
    d = [Data(1.27, 2.3),
         Data(2.25, 2.95),
         Data(2.5, 3.5),
         Data(3.6, 5.1)]
 
    # Size of dataset
    n = 4
 
    # Sample y value
    y = 4.5
 
    # Using the Inverse Interpolation
    # function to find the
    # value of x when y = 4.5
    print("Value of x at y = 4.5 :",
           round(inv_interpolate(d, n, y), 5))


#CUBIC SPLINE

import numpy as np
import sympy as sp

def ch(n):
  if n < 0:
    return '-'
  else:
    return '+'


n = int(input("Enter number of values : "))
x  = []
fx = []

for i in range(n):
  x.append(float(input("Enter x : ")))
  fx.append(float(input("Enter f(x) : ")))

'''n=4
x=[1,2,3,4]
fx=[1,5,11,8]'''

h = x[1] - x[0]
d = []

for i in range(1, n - 1):
  d.append(6 * (fx[i-1] - 2 * fx[i] + fx[i+1]) / (h*h) )

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
