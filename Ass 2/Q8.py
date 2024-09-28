num = -1 
while num <= 0:
    num = int(input("Enter a positive integer: "))
if num % 2 == 0:
    result = num * 2  
else:
    result = num ** 2  
print(f"The final result is: {result}")

