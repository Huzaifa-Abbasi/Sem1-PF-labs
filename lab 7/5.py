car_ids=[1,2,3,4,5]
car_names={1:"Suzuki Cultus",2:"Suzuki Alto",3:"Toyota Corolla", 4:"Honda City", 5:"Honda Civic"}
car_models={1:2020,2:2021,3:2020,4:2021,5:2020}
car_rentals={1:2000,2:1500,3:3000,4:2500,5:3500}
car_fuel={1:17,2:19,3:13,4:14,5:12}
car_issued={1:0,2:0,3:0,4:0,5:0}

user_input=""

while user_input!="q":
    print("Welcome to the ALI car rentals")
    print("\t\t\t ======== Available cars ========")
    print("#\tCar Name\t Model\t Fuel avg\t Rent/hour\t Available? ")
    for car in car_ids:
        print("{}\t{}\t{}\t\t{}\t{}\t\t{}".format(car,car_names[car],car_models[car],car_fuel[car],car_rentals[car],"Yes" if car_issued[car]==0 else "No"))
    print("Please make a choice (r to rent, t to return, q to quit)")
    user_input=input()
    if user_input=="r":
            c = int(input("Please enter car id to be rented: "))
            cnic = int(input("Please enter CNIC number: "))
            customer_name=input("Please enter customer name: ")
            car_issued[c]=1
            print("Car issued successfully!")
        
    if user_input=="t":
            c = int(input("Please enter car id to be returned: "))
            if car_issued[c]==1:
                car_issued[c]=0
            print("Car retuned successfully!")