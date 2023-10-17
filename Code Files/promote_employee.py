            # Import packages/modules: 

import re
import check_employee_id_exists as emp_exists
import Connection_Task as m

            # code:

def promote_employee(connection):

    print("                     ----->>> Promote Employee Details<<<-----                       \n")


    Id = input("Enter Employee ID: ")
    # if re.fullmatch(r"\d{5}", Id) is not None:
    #     print("Valid ID")
    if not emp_exists.employee_id_exits(Id, connection):                 # If Condition False
            print("Employee Id is Not Exists. \n   Please try again....")
            promote_employee(connection)
    else:
        print("1: Software Engineer")
        print("2: Software Associate Engineer")
        print("3: Senior Software Engineer")
        print("4: Technical Software Engineer")
        print("5: Technical Lead")
        print("6: Project Manager")
        designation_choice = int(input("Enter Designation Choice : "))
        if designation_choice == 1:
            print("Choice 1 is Software Engineer and Maximum Increament is 2000/- are you show want to promote :Yes/No ")
            emp_designation = "Software Engineer"
            Confirmation = input("Please Enter Your Confirmation : ")
            Confirm = Confirmation.lower()
            if Confirm == "yes":
                amount = 2000
            else:
                promote_employee()
        elif designation_choice == 2:
            print("Choice 2 is Software Associate Engineer and Maximum Increament is 4000/- are you show want to promote :Yes/No ")
            emp_designation = "Software Associate Engineer"
            Confirmation = input("Please Enter Your Confirmation : ")
            Confirm = Confirmation.lower()
            if Confirm == "yes":
                amount = 4000
            else:
                promote_employee()
        elif designation_choice == 3:
            print("Choice 3 is Senior Software Engineer and Maximum Increament is 6000/- are you show want to promote :Yes/No ")
            emp_designation = "Senior Software Engineer"
            Confirmation = input("Please Enter Your Confirmation : ")
            Confirm = Confirmation.lower()
            if Confirm == "yes":
                amount = 6000
            else:
                promote_employee()
        elif designation_choice == 4:
            print("Choice 4 is Technical Software Engineer and Maximum Increament is 8000/- are you show want to promote :Yes/No ")
            emp_designation = "Technical Software Engineer"
            Confirmation = input("Please Enter Your Confirmation : ")
            Confirm = Confirmation.lower()
            if Confirm == "yes":
                amount = 8000
            else:
                promote_employee()
        elif designation_choice == 5:
            print("Choice 5 is Technical Lead and Maximum Increament is 10000/- are you show want to promote :Yes/No ")
            emp_designation = "Technical Lead"
            Confirmation = input("Please Enter Your Confirmation : ")
            Confirm = Confirmation.lower()
            if Confirm == "yes":
                amount = 10000
            else:
                promote_employee()
        elif designation_choice == 6:
            print("Choice 6 is Project Manager and Maximum Increament is 12000/- are you show want to promote :Yes/No ")
            emp_designation = "Project Manager"
            Confirmation = input("Please Enter Your Confirmation : ")
            Confirm = Confirmation.lower()
            if Confirm == "yes":
                amount = 12000
            else:
                promote_employee()
        else:
            print("Invalid Choice Reason:\n     Choice not defined ", designation_choice)
            click = input("Press any key to continue further....")
    
        # amount = int(input("Enter Incremental Amount : "))

        # sql = "SELECT Salary FROM Emp_Data WHERE ID = %s"
        # data = (Id,)
        # c = connection.cursor()
        # c.execute(sql, data)

        sql = "SELECT Salary FROM Emp_Data WHERE ID = " + Id
        c = connection.cursor()
        c.execute(sql)
        f = c.fetchone()
        print("Fetch Current Salary :",f)
        i = f[0] + amount
        print("Fetch Increased Salary : ",i)
        sql_query = " UPDATE Emp_Data SET Designation = %s, Salary = %s WHERE ID = %s "
        values = (emp_designation, i,Id)
        c.execute(sql_query,values)
        connection.commit()
        print("Employee Details are Promoted Successfully in Emp_Data.")
    click = input("Press any key to continue further....")
    m.main_function(connection)







