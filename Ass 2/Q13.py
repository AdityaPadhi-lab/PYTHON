position = input("Enter a chess position (e.g., 'e4'): ")
if len(position) == 2 and position[0].lower() in 'abcdefgh' and position[1] in '12345678':
    column = position[0].lower()  
    row = int(position[1])         
    column_number = ord(column) - ord('a') + 1
    if (column_number + row) % 2 == 0:
        color = "White"
    else:
        color = "Black"
    print(f"The color of the square at {position} is {color}.")
else:
    print("Invalid position. Please enter a valid chess position (e.g., 'e4').")
def get_square_color(position):
    column = position[0].lower() 
    row = int(position[1])       
    column_number = ord(column) - ord('a') + 1
    if (column_number + row) % 2 == 0:
        return "White"
    else:
        return "Black"
position = input("Enter a chess position (e.g., 'e4'): ")
if len(position) == 2 and position[0].lower() in 'abcdefgh' and position[1] in '12345678':
    color = get_square_color(position)
    print(f"The color of the square at {position} is {color}.")
else:
    print("Invalid position. Please enter a valid chess position (e.g., 'e4').")
