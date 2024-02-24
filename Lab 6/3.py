my_list = []

for _ in range (5):
    user = int(input("Enter the Number: "))
    my_list.append(user)
    print(my_list)

even_sum = sum(num for num in my_list if num % 2 == 0)

if even_sum > 0:
    print("Sum of even numbers:", even_sum)
else:
    print("No even numbers in the list.")