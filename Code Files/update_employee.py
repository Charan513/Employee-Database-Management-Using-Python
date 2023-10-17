            # Import packages/modules: 

import check_employee_id_exists as emp_exists
import Connection_Task as m
import re

            # code:
            
def update_employee(connection):

    print("                     ----->>> Update Employee Details<<<-----                       \n")
    Id = input("Enter Employee ID: ")
    if emp_exists.employee_id_exits(Id, connection) == False:               # is False
            print("Employee Id is Not Exists. \n   Please try again....")
            m.main_function(connection)
    else:
        mailID = input("Enter Employee G-Mail ID: ")
        if re.fullmatch(r"\w+@gmail\.com", mailID) is not None:
            print("Valid Mail ID")
        else:
            print("Invalid Mail ID. Please enter a valid Gmail ID.")
            click = input("Press any key to continue further....")
            update_employee(connection)

        phone_number = input("Enter Employee Phone Number: ")    
        if re.fullmatch(r"(0|\\+91)?[6-9][0-9]{9}", phone_number) is not None:        
            print("Valid Phone Number")
        else:
            print("Invalid Phone Number. Please enter a valid phone number.")
            click = input("Press any key to continue further....")
            update_employee(connection)
        
        address = input("Enter Employee Address: ")
        if re.fullmatch(r"[\w\s.,:\-']+", address) is not None:     
            print("Valid Address")
        else:
            print("Invalid Address. Please enter a valid address.")
            click = input("Press any key to continue further....")
            update_employee(connection)
        

        # sql = "UPDATE Emp_Data SET Email_ID = " + mailID + "Phone_no = " + phone_number + "Address = " + address + "WHERE ID = " +Id
        sql = "UPDATE Emp_Data SET Email_ID = %s, Phone_no = %s, Address = %s WHERE ID = %s"

        data = (mailID, phone_number, address, Id)
        # Create a cursor to execute queries
        c = connection.cursor()
        # Execute the query with the value provided
        c.execute(sql, data)
        connection.commit()
        print("Employee Details are Updated Successfully into Employee Record.")
        click = input("Press any key to continue further....")
        m.main_function(connection)



    
