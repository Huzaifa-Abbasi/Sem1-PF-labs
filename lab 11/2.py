'''Create “lab11_2.py” and Create a Python program named "lab8_2.py" with a user-defined function called 
calculate_square. The function should take an integer as an argument and return the square of that 
number. Implement the program to fulfill the following requirement.'''

number = int(input("Enter the number: "))

def calculate_square(number):
    return number ** 2
square = calculate_square(number)
print(square)