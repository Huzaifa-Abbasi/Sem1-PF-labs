count = {}
sentence = input("Enter the sentence ")

for letter in sentence:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1

print(count)