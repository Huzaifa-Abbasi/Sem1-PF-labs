marks = int(input("Enter your obtain marks: "))
if marks < 40:
    print("Fail")
elif 41 <= marks <= 50:
    print("D grade")
elif 51 <= marks <= 60:
    print("C grade")
elif 61 <= marks <= 70:
    print("B grade")
elif 71 <= marks <= 80:
    print("A grade")
elif marks >= 81:
    print("A-1 grade")
