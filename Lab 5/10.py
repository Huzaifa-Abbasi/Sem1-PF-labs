no_of_terms = int(input("How many terms? "))
a, b = 0, 1
print(a, b, end=" ")
for i in range(2, no_of_terms):
    c = a + b
    print(c, end=" ")
    a, b = b, c
