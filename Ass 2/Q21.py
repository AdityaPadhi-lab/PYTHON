n = int(input("Enter an integer: "))
i = 1
factorial = 1
while factorial < n:
    i += 1
    factorial *= i
if factorial == n:
    print(f"{n} is a factorial number of {i}!")
else:
    print(f"{n} is not a factorial number. ")
