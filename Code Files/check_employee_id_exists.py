
            # code:

def employee_id_exits(Id, connection):
    sql = "SELECT * FROM Emp_Data WHERE Id = %s"
    c = connection.cursor(buffered = True)
    data = (Id,)
    c.execute(sql, data)
    count = c.rowcount
    # print("Employee Id Exists or Not Count : ", count)
    if count == 1:
        return True
    else:
        return False
    



















