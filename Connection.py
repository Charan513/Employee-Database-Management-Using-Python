            # Import packages/modules: 

import mysql.connector
from os import system
import add_employee as add
import display_employee as display
import update_employee as update
import promote_employee as promote
import remove_employee as remove
import search_employee as search



def main_function(connection):
    print("*********************************************************************************")
    print("                Employee Database Management                      ")
    print("*********************************************************************************")
    print("1: Add Employee To Database")
    print("2: Display Employee Data")
    print("3: Update Employee Data")
    print("4: Promote Employee Data")
    print("5: Remove Employee Data From Database")
    print("6: Search Employee Data")
    print("7: Exit")
    print("---------->>>> Choose Choices: [1 2 3 4 5 6 7]<<<<----------")
    choice = int(input("Enter Choice: "))

    if choice == 1:
        system("cls")
        add.add_employee(connection)
        main_function(connection)
    elif choice == 2:
        system("cls")
        display.display_employee(connection)
        main_function(connection)
    elif choice == 3:
        system("cls")
        update.update_employee(connection)
        main_function(connection)
    elif choice == 4:
        system("cls")
        promote.promote_employee(connection)
        main_function(connection)
    elif choice == 5:
        system("cls")
        remove.remove_employee(connection)
        main_function(connection)
    elif choice == 6:
        system("cls")
        search.search_employee(connection)
        main_function(connection)
    elif choice == 7:
        print("Thank you for your patience. Have a nice day!")
        exit(0)
    else:
        print("Invalid Choice Reason:\n     Choice not defined ", choice)
        click = input("Press any key to continue further....")
        main_function(connection)


if __name__ == "__main__":
    print("                     ----->>> Welcome to Employee Database Management <<<-----                       \n")
    username = input("Enter User Name: ")
    pwd = input("Enter User Password: ")
    database_name = input("Enter Database Name: ")

    # Establish a connection to the MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user=username,
        password=pwd,
    )

    # Create a cursor object to interact with the database
    mycursor = connection.cursor()

    # Create the 'Emp_details' database if it doesn't exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS " + database_name)
    connection = mysql.connector.connect(
        host="localhost",
        user=username,
        password=pwd,
        database=database_name,
    )

    # Create a cursor object to interact with the database
    cursor = connection.cursor()
    print("Connection Established Successfully with " + database_name + " Database......")
    
     # Create the 'Emp_Data' table if it doesn't exist
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS Emp_Data (ID int(11) AUTO_INCREMENT primary key, Name varchar(1800), Designation text(50), "
        "Email_ID text(1800), Phone_no bigint(11), Address varchar(1000), Post text(1000), Salary bigint(11))"
    )

    main_function(connection)
















































































