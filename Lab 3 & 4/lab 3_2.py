a = float(input("Enter the first number (A): "))
b = float(input("Enter the second number (B): "))
c = float(input("Enter the third number (C): "))

result1 = a + (b + c)
result2 = (a + b) + c
result3 = a * (b * c)
result4 = (a * b) * c

print("Associative", (a+(b+c) == (a+b)+c))