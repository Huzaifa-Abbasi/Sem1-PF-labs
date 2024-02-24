dict={
    "huzaifa":21,
    "umer":33,
    "talat":54,
    "ali":26,
}

user_name= input("Enter the user name ")
password= int(input("Enter the Password "))

if user_name in dict and password == dict[user_name]:
    print("log in successful")
else:
    print("iNVALID PASWORD OR USER NAME ")