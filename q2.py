# newton forward interpolation

def calc(u,n):
  temp=u;
  for i in range(1,n):
    temp=temp*(u-i);
  return temp;

def fact(n):
  f=1;
  for i in range(2,n+1):
    f=f*i;
  return f;


# Number of values given
n=4;
x=[45,50,55,60];

y = [[0 for i in range(n)]for j in range(n)];
y[0][0]=0.7071;
y[1][0]=0.7660;
y[2][0]=0.8192;
y[3][0]=0.8660;

for i in range(1,n):
  for j in range(n-i):
    y[j][i]=y[j+1][i-1]-y[j][i-1];

for i in range(n):
  print(x[i],end="\t");
  for j in range(n-i):
    print(round(y[i][j],4),end="\t");
  print("");

value = 52;

sum=y[0][0];
u=(value-x[0])/(x[1]-x[0]);
for i in range(1,n):
  sum=sum+(calc(u,i)*y[0][i])/fact(i);

print("\nValue at", value, "is", round(sum, 4));


# newton backwack interpolation

def calc(u,n):
  temp=u
  for i in range(n):
    temp=temp*(u+i)
  return temp

# Calculating factorial of given n
def fact(n):
  f = 1
  for i in range(2,n+1):
    f=f*i
  return f

# number of values given
n=5
x=[45,50,55,60,65];

# y is used for difference

y = [[0 for i in range(n)] for j in range(n)]
y[0][0]=114.84;
y[1][0]=96.16;
y[2][0]=83.32;
y[3][0]=74.48;
y[4][0]=68.48

# Calculating the backward difference table
for i in range(1,n):
  for j in range(n-1,i-1,-1):
    y[j][i]=y[j][i-1]-y[j-1][i-1]

# Displaying the backward difference table
for i in range(n): 
    print(x[i],end="\t");
    for j in range(i+1):
        print(round(y[i][j],4),end="\t") 
    print("")

# Value to interpolate at
value = 64

# Initializing u and sum
sum = y[n-1][0]
u=(value-x[n-1])/(x[1]-x[0])
for i in range(1,n):
  sum=sum+(calc(u,i)*y[n-1][i])/fact(i)

print("\nValue at",value,"is",round(sum,4))