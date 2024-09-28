n = int(input("Enter a positive integer: "))
reversed_number = 0
while n > 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n = n // 10
print("Reversed number:", reversed_number)
