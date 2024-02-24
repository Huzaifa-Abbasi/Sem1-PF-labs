import random

my_list = []

for _ in range(20):
    num = random.randint(1, 100)
    my_list.append(num)
print("Generated List:", my_list)

largest = my_list[0]
for num in my_list:
    if num > largest:
        largest = num

smallest = my_list[0]
for num in my_list:
    if num < smallest:
        smallest = num
        
print("Largest Number:", largest)
print("Smallest Number:", smallest)
