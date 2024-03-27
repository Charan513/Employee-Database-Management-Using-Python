
# Employee Database Management

## Overview

The "**Employee Database Management**" project is a Python-based console application designed to streamline the process of managing employee data in a MySQL database. It offers a set of essential functionalities for adding, viewing, updating, promoting, removing, and searching employee records. 

## Features

- **Add Employee**: Easily add new employee records to the database, complete with details like ID, name, designation, email ID, phone number, address, post address, and salary. Robust input validation ensures data integrity.

- **Display Employee Data**: View all employee records stored in the database, presented in a well-organized tabular format.

- **Update Employee Data**: Modify specific employee details such as email ID, phone number, and address. The application includes validation checks to maintain data accuracy.

- **Promote Employee Data**: Promote employees by selecting new designations and updating their salaries accordingly. The project offers predefined options for different designations and ensures accurate data handling.

- **Remove Employee Data**: Conveniently delete employee records by providing their ID. Validation confirms the existence of the ID before proceeding with deletion.

- **Search Employee Data**: Easily find a specific employee by entering their employee ID. If the ID is in the database, the application displays their details.

## Project Structure

The project is structured into modular components, each serving a specific function:

- `Connection_Task.py`: Manages the connection to the MySQL database and presents a user-friendly menu for selecting tasks.
- `add_employee.py`, `display_employee.py`, `update_employee.py`, `promote_employee.py`, `remove_employee.py`, and `search_employee.py`: Corresponding modules for each of the project's functionalities.

## Input Validation

The application employs regular expressions for input validation, ensuring that user-provided data conforms to specified formats, such as ID, email ID, and phone number. This guarantees data accuracy and integrity.


## Author

[Kandukuri Charan](https://github.com/Charan513)
    
