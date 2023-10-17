
            # code:

def employee_name_exists(EmpName, connection):
    sql = "SELECT * FROM Emp_Data WHERE Name = %s"
    c = connection.cursor(buffered = True)
    data = (EmpName,)
    c.execute(sql, data)
    count = c.rowcount
    # print("Employee Name Exists or Not Count : ", count)
    if count == 1:
        return True
    else:
        return False


