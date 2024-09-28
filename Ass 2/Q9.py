user_input = input("Enter an integer: ")

if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
    num = int(user_input)
    match num % 5:
        case 0:
            result = "The remainder is 0."
        case 1:
            result = "The remainder is 1."
        case 2:
            result = "The remainder is 2."
        case 3:
            result = "The remainder is 3."
        case 4:
            result = "The remainder is 4."
    
    print(result)
else:
    print("Invalid input")
