# cbms
Cab booking managemen system using Python and mySql.

# Cab Booking System (Python + MySQL)

## 📌 Overview
This project is a simple **Cab Booking System** built with Python, MySQL, and Pandas/Matplotlib for data visualization.  
It demonstrates:
- User authentication
- Menu-driven program flow
- Database integration for booking and availability
- Basic data visualization of available vehicles

---

## ⚙️ Features
1. **Login System**
   - Admin credentials: `admin` / `test1`
   - Verifies before granting access to the system

2. **Cab Booking**
   - Collects customer details (Name, Mobile, Location, Gender)
   - Stores booking information in MySQL database (`cab` table)

3. **Check Availability**
   - Queries the `available` table in MySQL
   - Displays cab availability and prices by state

4. **Available Vehicles**
   - Shows a DataFrame of vehicle types and counts
   - Generates a bar chart using Matplotlib

5. **Exit Option**
   - Cleanly terminates the program

---

## 🛠️ Tech Stack
- **Python 3**
- **MySQL Connector (mysql-connector-python)**
- **Pandas**
- **Matplotlib**

---

## 📂 Database Setup
Create a MySQL database named `cab` with the following tables:



### Table: `cab`
```sql
CREATE TABLE cab (
    CustomerName VARCHAR(50),
    MobileNumber VARCHAR(15),
    Location VARCHAR(50),
    Gender VARCHAR(10)
);


```available
CREATE TABLE available (
    State VARCHAR(50),
    Availability VARCHAR(20),
    Price DECIMAL(10,2)
);


```how to run
1. Install dependencies
pip install mysql-connector-python pandas matplotlib

2. Configure mysql connection inside the script, password should be your mysql password
connection = msq.connect(user="root", passwd="your_password", host="localhost", database="cab")

3. Run the program.
python cab_booking.py


