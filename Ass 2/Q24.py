num = int(input("Enter an integer: "))
unique_digits = []
while num > 0:
    digit = num % 10
    if str(digit) not in unique_digits:
        unique_digits.append(str(digit))
    num //= 10
for digit in sorted(unique_digits):
    if digit == '0':
        print('ZERO', end=' ')
    elif digit == '1':
        print('ONE', end=' ')
    elif digit == '2':
        print('TWO', end=' ')
    elif digit == '3':
        print('THREE', end=' ')
    elif digit == '4':
        print('FOUR', end=' ')
    elif digit == '5':
        print('FIVE', end=' ')
    elif digit == '6':
        print('SIX', end=' ')
    elif digit == '7':
        print('SEVEN', end=' ')
    elif digit == '8':
        print('EIGHT', end=' ')
    elif digit == '9':
        print('NINE', end=' ')