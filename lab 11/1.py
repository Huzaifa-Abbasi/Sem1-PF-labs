'''Open Python IDLE terminal and then create a new file. Name it “lab11_1.py”. write a program with a 
user-defined function which takes a string as argument and returns reverse of string.'''


def rev_str(sentence):
    return sentence [::-1]
sentence = input("Enter a sentence: ")
rev = rev_str(sentence)

print(sentence)
print(rev)