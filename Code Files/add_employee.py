            # Import packages/modules: 

import re
import Connection_Task as m
import check_employee_id_exists as emp_exists
import check_employee_name_exists as name_exists

            # code:

def add_employee(connection):
    print("                     ----->>> Welcome to Add Employee Database<<<-----                       \n")


    Id = input("Enter Employee ID: ")
    if re.fullmatch(r"\d{5}", Id) is not None:
        print("Valid ID")
        if emp_exists.employee_id_exits(Id, connection):
            print("Employee Id Already Exists. \n   Please try again....")
            add_employee(connection)
    else:
        print("Invalid ID. Please enter exactly 5 digits.")
        click = input("Press any key to continue further....")
        add_employee(connection)


    EmpName = input("Enter Employee Name: ")
        # Convert all letters into small.
    lower = EmpName.lower()
        # Make the first letter into capital.
    title = lower.title()
        # Assign the capitalized name back to EmpName
    EmpName = title         

    if re.match(r"[a-zA-Z\s]+", EmpName) is not None:
        print("Valid Name")
        if name_exists.employee_name_exists(EmpName, connection):
            print("Employee Name Already Exists. \n   Please try again....")
            add_employee(connection)
    else:
        print("Invalid Name. Please enter only letters.")
        click = input("Press any key to continue further....")
        add_employee(connection)


    designation = input("Enter Employee Designation : ")
        # Convert all letters into small.
    # Lower = designation.lower()
        # Make the first letter into capital.
    # Title = Lower.title()
        # Assign the capitalized name back to designation
    # designation = Title
    if re.match(r"[a-zA-Z\s]+", designation) is not None:           # Condition will be True.
        print("Valid Desination")
    else:
        print("Invalid Designation. Please enter a valid Designation.")
        click = input("Press any key to continue further....")
        add_employee(connection)


    mailID = input("Enter Employee G-Mail ID: ")
    if re.fullmatch(r"\w+@gmail\.com", mailID) is not None:
        print("Valid Mail ID")
    else:
        print("Invalid Mail ID. Please enter a valid Gmail ID.")
        click = input("Press any key to continue further....")
        add_employee(connection)


    phone_number = input("Enter Employee Phone Number: ")
    """ 
     The backslash "\\" is used to escape the plus sign "+" since it is a special character in regular expressions.
     ? --- > Is optional. Means (0|\\+91) are optional if we enter or not the input function it will take.
    """
    if re.fullmatch(r"(0|\\+91)?[6-9][0-9]{9}", phone_number) is not None:        
        print("Valid Phone Number")
    else:
        print("Invalid Phone Number. Please enter a valid phone number.")
        click = input("Press any key to continue further....")
        add_employee(connection)


    address = input("Enter Employee Address: ")
    """ 
        This RegEx will match addresses that contain any combination of letters, 
        digits, underscores, whitespace characters (spaces), Dots/periods, colons,
        commas, single quotes, and hyphens. 
    """
    if re.fullmatch(r"[\w\s.,:\-']+", address) is not None:     
        print("Valid Address")
    else:
        print("Invalid Address. Please enter a valid address.")
        click = input("Press any key to continue further....")
        add_employee(connection)


    post_address = input("Enter Employee Post Address: ")
    if re.fullmatch(r"\d{6}", post_address) is not None:
        print("Valid Post Address")
    else:
        print("Invalid Post Address. Please enter a valid Post address.")
        click = input("Press any key to continue further....")
        add_employee(connection)


    salary = input("Enter Employee Salary: ")
    if re.fullmatch(r"\d{1,5}", salary) is not None:       # (0-9)
        print("Validated Salary")
    else:
        print("Invalid salary. Please enter a valid salary.")
        click = input("Press any key to continue further....")
        add_employee(connection)


    # Create a cursor to execute queries
    c = connection.cursor()
    employee_data = (Id, EmpName, designation, mailID, phone_number, address, post_address, salary)
    sql_query = "INSERT INTO Emp_Data VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    # Execute the query with the value provided
    c.execute(sql_query, employee_data)
    connection.commit()


    print("Employee Data Added Successfully to Employee Record.")
    click = input("Press any key to continue further....")
    # add_employee(connection)
    m.main_function(connection)



