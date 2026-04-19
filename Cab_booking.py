import mysql.connector as msq
import pandas as pd
import matplotlib.pyplot as pl

# Login
N = input("UserName : ")
P = input("Password : ")

print("\n---------------------------------------------------------------\n")

if N == "admin" and P == "test1":
    print("Credentials Verified")
    print("\n---------------------------------------------------------------")
    print("Welcome to the Program Admin")
    print("---------------------------------------------------------------\n")

    Choice = 0
    while Choice != 4:
        Choice = int(input(" 1. Book Your Cab\n 2. Check Availability Of Cab\n 3. Available With Us\n 4. Exit The Program\n\n Please select your choice: "))

        if Choice == 1:
            print("\n------------------ Book Your Cab ------------------\n")
            connection = msq.connect(user="root", passwd="sshw7968", host="localhost", database="cab")
            cur = connection.cursor()

            cname = input("Customer Name : ")
            mno = input("Mobile Number : ")
            loc = input("Location : ")
            gen = input("Gender (Male/Female/Other) : ")

            query1 = "INSERT INTO cab (CustomerName, MobileNumber, Location, Gender) VALUES (%s, %s, %s, %s)"
            cur.execute(query1, (cname, mno, loc, gen))
            connection.commit()

            print("Booking Done\n---------------------------------------------------------------\n")

        elif Choice == 2:
            print("\n------------------ Check Availability ------------------\n")
            connection = msq.connect(user="root", passwd="sshw7968", host="localhost", database="cab")
            cur = connection.cursor()

            state = input("Enter Your State : ")
            query2 = "SELECT Availability, price FROM available WHERE State = %s"
            cur.execute(query2, (state,))
            data = cur.fetchall()

            print("Availability Status & Prices:\n--------------------------------------------")
            for i in data:
                print(i)
            print("\n---------------------------------------------------------------\n")

        elif Choice == 3:
            print("\n------------------ Available With Us ------------------\n")
            ac = {
                "S No.": [1, 2, 3, 4, 5, 6],
                "Type Of Vehicles": ['SUV', 'Sedan', 'Hatchback', 'Luxury Cars', 'Micro', 'Wagon'],
                "Total Cars": [18, 45, 25, 9, 29, 14]
            }
            cabdata = pd.DataFrame(ac)
            print(cabdata)

            m = ['SUV', 'Sedan', 'Hatchback', 'Micro']
            n = [18, 45, 25, 29]
            pl.xlabel("Types Of Vehicles")
            pl.ylabel("Total Cars")
            pl.bar(m, n, color="c")
            pl.show()
            print("\n---------------------------------------------------------------\n")

        elif Choice == 4:
            print("Exiting Program...")
            break

else:
    print("Verify Your Credentials and Try Again")
