# lab5_7.py

num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if (num % i) == 0:
            print(num, "is not a prime number.")
    else:
        print(num, "is a prime number.")