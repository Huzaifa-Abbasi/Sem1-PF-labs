student = {}
for i in range(1,3):
    name = input("Enter Name to add ")
    marks = int(input("Enter enter marks "))
    student [i] = {"Name ":name, "marks ":marks}
    student[name]=marks
name_1 = input("Enter name to check Marks ")
if name_1 in student.keys():
    print("Students Is Present ",student[name_1])
else:
    print ("No Student ")
