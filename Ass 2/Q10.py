input_string = input("Enter a string: ")
substrings = []
for i in range(len(input_string)):
    for j in range(i + 1, len(input_string) + 1):
        substrings.append(input_string[i:j])
for substring in substrings:
    print(substring)
