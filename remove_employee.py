            # Import packages/modules: 

import check_employee_id_exists as emp_exists
import re
import Connection_Task as m

            # code:

def remove_employee(connection):

    print("                     ----->>> Remove Employee Details<<<-----                       \n")


    Id = input("Enter Employee ID: ")
    if re.fullmatch(r"\d{5}", Id) is not None:
        print("Valid ID")
        if not emp_exists.employee_id_exits(Id, connection):                 # If Condition False
            print("Employee Id is Not Exists. \n   Please try again....")
            remove_employee(connection)
    
    sql = "DELETE FROM Emp_Data WHERE ID = "+ Id
    # sql = "DELETE FROM Emp_Data WHERE ID = %s"
    # data = (Id,)

    # Create a cursor to execute queries
    c = connection.cursor()

    # Execute the query with the value provided
    c.execute(sql)
    # c.exceute(sql, data)
    connection.commit()
    print("Employee Details are Deleted Successfully in Emp_Data.")
    click = input("Press any key to continue further....")
    m.main_function(connection)


    
