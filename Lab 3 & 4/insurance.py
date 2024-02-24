age = int(input("Enter your age: "))
employment_status = input("Enter your employment status: ")
marital_status = input("Enter your marital status: ")

if age < 25 or employment_status == "any":
    print("Not allowed")
elif 25 <= age <= 40 and employment_status == "unemployed" and marital_status == "unmarried":
    print("Insurance plan: 800 PKR/month")
elif 25 <= age <= 40 and employment_status == "unemployed" and marital_status == "married":
    print("Insurance plan: 1200 PKR/month")
elif 25 <= age <= 40 and employment_status == "employed" or age > 40 and marital_status == "married":
    print("Insurance plan: 1000 PKR/month")
else:
    print("Insurance plan: 1500 PKR/month")