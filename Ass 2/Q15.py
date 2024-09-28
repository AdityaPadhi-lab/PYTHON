number = int(input("Enter a natural number: "))
sum_of_divisors = 0
for i in range(1, number):
    if number % i == 0:
        sum_of_divisors += i
if sum_of_divisors == number:
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
num=int(input("enter a number \n"))
sumofdevisor=0
for i in range (1,num):
    if(num%i==0):
        sumofdevisor+=i
        if (sumofdevisor==num):
         print("yes its a perfect no: ")
        else:
           print("no its not a perfectno:  ")
