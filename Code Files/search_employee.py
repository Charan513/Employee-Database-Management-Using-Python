            # Import packages/modules: 

import re
import Connection_Task as m
import check_employee_id_exists as emp_exists

            # code:

def search_employee(connection):

    print("                     ----->>> Search Employee Details<<<-----                       \n")
    Id = int(input("Enter Employee Id : "))
    # if re.fullmatch(r"\d{5}", Id) is not None:
    #     print("Valid ID")
    if not emp_exists.employee_id_exits(Id, connection):                 # If Condition False
        print("Employee Id is Not Exists. \n   Please try again....")
        search_employee(connection)
    
    sql = "SELECT * FROM Emp_Data WHERE ID = " + str(Id)
    # sql = "SELECT * FROM Emp_Data WHERE ID = %s"

    c = connection.cursor()
    # c.execute(sql, (Id,))
    # c.execute("SELECT * FROM Emp_Data")
    c.execute(sql)
    results = c.fetchall()
    for i in results:
        print("Employee Id : ",i[0])
        print("Employee Name : ",i[1])
        print("Employee Designation : ",i[2])
        print("Employee Mail Id : ",i[3])
        print("Employee Phone Number : ",i[4])
        print("Employee Address : ",i[5])
        print("Employee Post Address : ",i[6])
        print("Employee Salary : ",i[7])
        print("\n")
    print("Search Employee Details are Fetched Successfully .......")
    click = input("Press any key to continue further....")
    m.main_function(connection)











