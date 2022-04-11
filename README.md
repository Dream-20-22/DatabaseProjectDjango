Project Specification:

Teams will design and implement a web-based university course management system. 
The system will make use of the university database that you have been working on since the beginning of this semester. 
The system will utilize the Django web framework to connect to MySQL and to hold together all components: 
loading data from database and dynamically creating a web page for displaying the data. The user interface will be built using Django templates.


Your system will provide functionalities for three kinds of users: admin, prof, and students, as follows:

Admin can do the following: 
F1. Create a list of professors sorted by one of the following criteria chosen by the admin: (1) by name (2) by dept, or (3) by salary 
F2. Create a table of min/max/average salaries by dept 
F3. Create a table of professor name, dept, and total number of students taught by the professor in a given semester 

Professors can do the following: 
F4. Create the list of course sections and the number of students enrolled in each section that the professor taught in a given semester 
F5. Create the list of students enrolled in a course section taught by the professor in a given semester 

Students can do the following: 
F6. Query the list of course sections offered by dept in a given semester and year.

To run this code, you need following things to do:
Install Python and mysql-connector-python
Installing and using Django
setup the connection
Python IDE to execute and run the project(you can use pycharm)
Change the password of mysql in settings.py and views.py
run the command python manage.py runserver 
or python3 manage.py runserver
That's all
