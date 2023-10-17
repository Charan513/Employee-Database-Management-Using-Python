						 	    Employee Database Management System                      
           				       	    ***************************************************  
This project is all about how to maintain the employee details in the Mysql Database .

Created 	: Kandukuri Charan 
Date    	: July 03 2023
Organization    : Calc Technology
Location 	: Nandyal
College  	: National Degree College 
*****************************************************************************************************************************
Discription :  Here the main activity of this project is "Employee Database Management" and below activities in this project .
-----------
		 Main Method 		   1.Add Employee to Database
		   2.Display Employee Data
		   3.Update Employee Data
		   4.Promote Employee Data
		   5.Remove Employee Data From Database
		   6.Search Employee Data
		   7.Exit
Main Method :  This is the main method of the project where complete project works from here . In this method database connection preparation , input to connect with 			database and finally Database name and database table are going to be created .
			Input   :- Database username, Database Password and Database Name.
			Process :- Database connection with user name and Password, Database to work on and table (empdata)to work on. 
					+-------------+---------------+------+-----+---------+-------+
                                        | Field       | Type          | Null | Key | Default | Extra |
                                        +-------------+---------------+------+-----+---------+-------+
                                        | Id          | int           | NO   | PRI | NULL    |       |
                                        | Name        | varchar(1800) | YES  |     | NULL    |       |
                                        | Designation | tinytext      | YES  |     | NULL    |       |
                                        | Email_Id    | text          | YES  |     | NULL    |       |
                                        | Phone_no    | bigint        | YES  |     | NULL    |       |
                                        | Address     | text          | YES  |     | NULL    |       |
                                        | Post        | text          | YES  |     | NULL    |       |
                                        | Salary      | bigint        | YES  |     | NULL    |       |
                                        +-------------+---------------+------+-----+---------+-------+
			Output  :- Employee choices, Based on choice of the Administration. 
The First execution will be main.py. In this method adminidtrator will be giveing input as DB user name and Password along with this has to provide the DataBase name. With these data adminitrator will be able to create employee table. Once the table created providing choices to user. Below are the choices will be displayed to
 user.		1: Add Employee to Database
2: Display Employee Data
3: Update Employee Data
4: Promote Employee Data
5: Remove Employee Data From Database
6: Search Employee Data
7: Exit
		------->>>> Choose Choices: [1 2 3 4 5 6 7] <<<<-------

Based on the choices user can be availed above 7 functionalities.

If user/administrator chooses choice 1 he/she can availed "Add Employee to Database".
  1.Add Employee to Data Base : This is the main functionallity where we can add employee details into the database. In this function we collect the details of
                                   the  employee and add them in the database . In the below there are the details which are going to be captured. 
		     1.1 Input:- Employee Id , Employee Name, Employee Designation, Employee Email id, Employee Phone number, Employee Address, Employee Post,    					                 Employee Salary. 
				   Employee Id       :- The "Employee Id "  is the unique Id, where it should not be the same as any other employee Id.
				   Employee Name     :- In the "Employee Name" the first letter should be capital and the remaining letters should be small. 	
								    EX :- Hari
				   Employee Designation :- It is input here we collect the "Employee Designation"and it should accept the required criteria.
								 -> it does not consist numericals and special character.
								 ->  It only accept the alphabets. 
								    EX:- Software Engineer
				   Employee Email id :- This is input here we can collect the employee email id and it should accept the required criteria. 
								    It should be alphabets(upper and lower case), number in addition to that @gmail.com.
								    EX :- hari97854@gmail.com
				   Employee Phonenumber:- This input is to collect the phone number of employee to communicate if required.
							   It should start with either (6,7,8,9)+9Digits. 
							   It should not contain any alphabet and special character.
 	        	 	   				    EX :- 9491207002
				   Employee Address  :- This is input that addresses that contain any combination of letters,digits, underscores, whitespace     							 -characters(spaces),Dots/periods, colons, commas, single quotes,and hyphens. 
								    EX :- Hno:1-122 , Hyderabad
				   Employee Post     :- This  is input  to collect the post adress of an employee. 
								It does not consist/allow any type af alphabet and special character.
								It contain only the nummeric data and consider only 6 digits. 
								    EX :- 500001
				   Employee Salary   :- This  is input  to collect the information of employee salary.
							     It does not consist/allow  any type af alphabet and special character.
							     It contain only the nummeric data upto 7 digits 
								 EX :- 45000
		  1.2 Process:- Database connection, sql Query and execution. 					  	
				 Database connection: Means provide a connection between the Main Method and the database server,when ever the user enter the 						              database name.
						     -> A sever that checks the database to see if the given database name exist or not,
							if the Database name exist then the sever connect the main method to it.
						     -> If the Database name does not exist it may create a new Database with the given name.
 				       Sql Query    : It is command that help to add the employee details into the Database.
				          execution : Here the input and Sql Query for add employee is going to be executed.
		 1.3 Output:- The Employee Details are successfully added to the Employee Record.
	         1.4       : once the add employee to the database method success then navigating to main method again and asking choices tothe user/administrator.

If user/administrator chooses choice 2 he/she can availed "Display Employee Data".
  2.Display Employee Data : This is the functionality where we can see that all the employees are exist in our database .Here there are few inputs required to 			            display employee details.
		 2.1 Input   : In this method no input data are collecting.
		 2.2 Process : Database connection, sql Query and execution
				 Database connection:It provide a connection between the  Main Method and the user defined database server. 
				        Sql Query   : It is command that help to display all the employee records from the Database.
				        execution   : Here the execution takes place according to the user choice(select display employee option)and after choice Sql 							Query for Display employee is going to be executed.
		 2.3 Output  : The Employee Details are successfully displayed from the  Employee Record.
		 2.4         : once the display employee to the database method success then navigating to main method again and asking choices tothe 					       user/administrator.

If user/administrator chooses choice3 he/she can availed "Update Employee Data".
  3.Update Employee Data : This is the functionality where we can update all the employees records in the Database, Here there are few inputs required to Update 			     Employee details.
		  3.1 Input   : In this method input is Employee Id, Employee Email id, Employee Phone number and Employee Address.
		  3.2 Process : Database connection, sql Query and execution
  				Database connection:It provide a connection between the  Main Method and the user defined database server. 
				Sql Query          : It is command that help to Update employee records in the Database.
         			execution  	   : Here the input and Sql Query of update employee is going to be executed.
		  3.3 Output  : Employee data is sucessfully updated into the Employee record.
		  3.4         : once the Update employee to the database method success then navigating to main method again and asking choices tothe 					        user/administrator.

If user/administrator chooses choice3 he/she can availed "Promote Employee Data".
  4.Promote Employee Data : This is the functionality where we can promote all the employees records in the Database, Here there are few inputs required to Promote                        			      Employee details .
 		  4.1 Input   : In this method input is Employee Id  and Designation choice.
                  4.2 Process : Database connection, sql Query and execution.
				Database connection:It provide a connection between the Main Method and the user defined database server.
				Sql Query          : It is command that help to  Promote employee records in the Database.
				execution  	   : Here the input (it must consist valid Employee Id and Designation choice )and Sql Query of update employee is 						     going to be executed.
						    ->	If the Employee Id is not valid Id then the execution may not takes place.
						    ->  If the Employee Id is valid, then only it promotes the Designation and salary of the employee.
		  4.3 Output : Employee salary is successfully promoted into the employee record.
		  4.4        : once the Promote employee to the database method success then navigating to main method again and asking choices tothe 					       user/administrator.

If user/administrator chooses choice3 he/she can availed "Remove Employee Data From Database".
  5.Remove Employee Data From Data Base : This is the functionality where we can remove all the employees records from the Database, Here there are few inputs 					  required to Remove Employee Data From Data Base.
		  5.1 Input   : In this method input is  Employee Id. 
		  5.2 Process : Database connection, sql Query and execution.
				Database connection:It provide a connection between the  Main Method and the user defined database server.
				Sql Query          : It is command that help to  remove employee records from the Database.
				execution  	   : Here the input and Sql Query of update employee is going to be executed.
 							-> If the Employee Id is not valid Id then the execution may not takes place.
							-> If the Employee Id is valid, then only execution may takes place.
		   5.3 Output : successfully the employee record has been removed from  your the Database.
		   5.4        : once the remove employee from the database method success then navigating to main method again and asking choices tothe 					user/administrator.

If user/administrator chooses choice3 he/she can availed "Search Employee Data".
   6.Search Employee Data : This is the functionality where we can search all the employees records in the Database, Here there are few inputs 					    required to Search an Employee From Data Base.
		  6.1 Input   : In this method input is  Employee Id.
		  6.2 Process : Database connection, sql Query and execution
				Database connection:It provide a connection between the  Main Method and the user defined database server
				Sql Query          : It is command that help to  search an employee records from the Database.
		                execution          : Here the input and Sql Query of update employee is going to be executed.
 							-> If the Employee Id is not valid Id then the execution may not takes place.
							-> If the Employee Id is valid, then only execution may takes place.
   		 6.3 Output  : The Searching of an Employee from  employee records is successfully done.
		 6.4         : once the searching an employee from the database method is success then navigating to main method again and asking choices tothe 			       user/administrator.

 If user/administrator chooses choice3 he/she can availed " Exit".
   7.Exit : This is the functionality where we can exit from the Database, Here there are few inputs are required . 
		 7.1 Input   : In this method no input data are collecting.
		 7.2 Process : Database connection ,Sql Query and execution
				     Database connection :  Here  Database connection must provid a exit facilities to a connection between the  Main Method and the 							    user defined database server .
					Sql Query        :  No query is written in this mode .
  				     execution           :  Here the execution takes place according to the user choice( Whenever user select exit function option) .
		 7.3 Output : Thank You For Your Patience 
                                              Have a Nice Day !!! 
				        Bye !                    
         	 7.4        : Now the user exit from the Database.

                                      ******************************************************************************
				  
