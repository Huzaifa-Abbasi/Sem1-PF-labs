list = []
for i in range (1, 50):
    list.append(i)
print(list)
for i in list:
    if i % 2 == 0:
        print("square",i**2)
    elif i % 2 != 0:
        print("cube",i**3)