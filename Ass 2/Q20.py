n = int(input("Enter an integer: "))
factors = []
i = 2
while n > 1:
    while n % i == 0:
        factors.append(i)
        n = n // i
    i += 1
print("Factors in increasing order:", factors)
