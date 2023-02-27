from fractions import Fraction
import math

def f_(x):
  #f_value = (1/(1+x**2))
  f_value = math.log(x,math.e)
  #f_value = math.exp(-x**2)
  return f_value

h = Fraction(input("Enter h : "))
ll = float(input("Enter Lower Limit : "))
ul = float(input("Enter Upper Limit : "))


#y_x values
y_x_ = []
n = int((ul - ll) / h)   #number of parts
#x_ = x values
x_ = ll
while(x_ < ul+h):
  y_x_.append(f_(x_))
  x_ += h

#TRAPEZOIDAL RULE

result1 = h/2*(y_x_[0]+y_x_[-1]+2*sum(y_x_[1:-1]))
print("Value of integral using Trapezoidal Rule : ",round(result1,3))


#SIMPSON'S 1/3 RULE

result2 = 0
term1 = [y_x_[0],y_x_[-1]]
term2 = []
term3 = []
for i in range(1,len(y_x_)-1):
  if (i%2==0):
    term2.append(y_x_[i])
  else:
    term3.append(y_x_[i])
#print(term1)
#print(term2)
#print(term3)
result2 = h/3*(sum(term1)+2*sum(term2)+4*sum(term3))
print("Value of integral using Simpson's 1/3 Rule : ",round(result2,3))


#SIMPSON'S 3/8 RULE

if (n%3!=0):
  print("Simpson's 3/8 rule is not applicable, as n is not a multiple of 3")
else:
  term1 = [y_x_[0],y_x_[-1]]
  term3 = y_x_[n//2]
  term2 = y_x_[1:-2]
  term2.remove(term3)
  print(term3)
  print(term2)
  print(term1)
  result3 = (3/8)*(h)*(sum(term1)+3*sum(term2)+2*(term3))
  print("Value of integral using Simpson's 3/8 Rule : ",round(result3,3))
