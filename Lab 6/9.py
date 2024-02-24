student_grades = {
        "ali": "A",
        "sam": "B",
        "alex": "C"
    }

student_name = input("Enter a student name: ")

if student_name in student_grades:
    print(f"The grade for {student_name} is: {student_grades[student_name]}")
else:

    print("Student not found.")
