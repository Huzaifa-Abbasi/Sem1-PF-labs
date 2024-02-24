num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# positive and negative
if num1 > 0 and num2 > 0:
    print("Both numbers are positive.")
elif num1 > 0 or num2 > 0:
    print("At least one of the numbers is negative.")
else:
    print("Neither of the numbers is positive.")

# at least one is positive or negative
if num1 > 0 or num2 > 0:
    print("At least one of the numbers is positive.")
elif num1 < 0 or num2 < 0 :
    print("At least one of the numbers is Negative.")


# even
if num1 % 2 == 0 and num2 % 2 == 0:
    print("Both numbers are even.")
elif num1 % 2 == 0 or num2 % 2 == 0:
    print("At least one of the numbers is even.")
elif num1 % 2 == 0 or num2 % 2 == 0:
    print("At least one of the numbers is even.")
else:
    print("Neither of the numbers is even.")

# odd
if num1 % 2 != 0 and num2 % 2 != 0:
    print("Both numbers are odd.")
elif num1 % 2 != 0 or num2 % 2 != 0:
    print("At least one of the numbers is odd.")
else:
    print("Neither of the numbers is odd.")

# At least one of them is odd
if num1 % 2 != 0 or num2 % 2 != 0:
    print("At least one of the numbers is odd.")
else:
    print("Neither of the numbers is odd.")

# Multiple of 3
if num1 % 3 == 0 and num2 % 3 == 0:
    print("Both numbers are multiples of 3.")
elif num1 % 3 == 0 or num2 % 3 == 0:
    print("At least one of the numbers is a multiple of 3.")
else:
    print("Neither of the numbers is a multiple of 3.")
    