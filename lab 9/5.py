student = {}
for i in range(1, 4):
    roll_number = int(input("Enter The Roll Number of student "))
    student_name = input("Enter The name of student ")
    

    if roll_number in student:
        print("this Number is already Added")
    else:
        student[roll_number] = student_name
        print(student)