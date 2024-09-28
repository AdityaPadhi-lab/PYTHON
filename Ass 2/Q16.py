import math
n=int(input("Enter value of n: "))
x=float(input("Enter value of x: "))
p=-1
sum=1
for i in range(2,n+1,2):
    #print(i)
    n2=p*(pow(x,i)/math.factorial(i))
    #print(f"at {i} n2 {n2}")
    p*=-1
    sum+=n2
print(f"Final Sum: {sum}")
