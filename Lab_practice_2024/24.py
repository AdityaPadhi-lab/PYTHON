a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))

min_val = min(a, b, c)
max_val = max(a, b, c)

mid_val = (a + b + c) - min_val - max_val

print("The numbers in sorted order are:", min_val, mid_val, max_val)
