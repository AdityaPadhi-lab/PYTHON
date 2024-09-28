num = int(input("Enter a number: "))

sum_of_primes = 0

for number in range(2, num): 
    is_prime = True  
    for i in range(2, int(number**0.5) + 1):  
        if number % i == 0:  
            is_prime = False
            break
    if is_prime:
        sum_of_primes += number  

print(f"Sum of all prime numbers less than {num} is {sum_of_primes}.")
