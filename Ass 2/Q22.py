number = int(input("Enter a number: "))
while number >= 10:
    total_sum = 0
    while number > 0:
        total_sum += number % 10
        number //= 10
    number = total_sum
print(f"The single-digit sum is: {number}")
