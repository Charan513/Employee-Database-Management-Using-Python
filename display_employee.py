            # Import packages/modules: 

import Connection_Task as m

            # code:

def display_employee(connection):

    print("                     ----->>> Display Employee Details<<<-----                       \n")    
    sql = "SELECT * FROM Emp_Data"
    # Create a cursor to execute queries
    c = connection.cursor()
    # Execute the query with the value provided
    c.execute(sql)

    # Fetch the results
    data = c.fetchall()
    # print("Number of count ", data)

    for i in data:
        print("Employee Id : ",i[0])
        print("Employee Name : ",i[1])
        print("Employee Designation : ",i[2])
        print("Employee Mail Id : ",i[3])
        print("Employee Phone Number : ",i[4])
        print("Employee Address : ",i[5])
        print("Employee Post Address : ",i[6])
        print("Employee Salary : ",i[7])
        print("\n")
    click = input("Press any key to continue further....")
    m.main_function(connection)





