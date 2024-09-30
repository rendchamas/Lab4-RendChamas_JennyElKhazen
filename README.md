# Lab4-RendChamas_JennyElKhazen
A project combining Tkinter and PyQt documented implemetations.

School Management System

Overview:
This project is a School Management System that allows users to manage students, instructors, and courses. It includes functionality for registering students, assigning instructors to courses, and handling course enrollments. The system offers two graphical user interfaces (GUIs) for interaction:




Tkinter Interface




PyQt Interface




Both interfaces allow you to add, edit, and delete records, as well as perform tasks like course enrollment, instructor assignment, and data export.

Requirements
Before running the application, ensure that you have the following dependencies installed:

Python 3.x
SQLite3 (pre-installed with Python)
Required Python packages:

pip install PyQt5
pip install pickle

How to Run:

1. Running the Tkinter Interface
The Tkinter interface provides basic functionality for managing students, instructors, and courses. To run the Tkinter interface:

Navigate to the project directory:
cd /path/to/project
Run the Tkinter version of the application:
python tkinter_school_management_system.py
This will open the Tkinter GUI where you can perform the following tasks:

Add students, instructors, and courses
View existing records
Register students to courses
Assign instructors to courses
Export data to CSV
Save/load records from a file
2. Running the PyQt Interface
The PyQt interface offers a more advanced and flexible user experience with additional functionality. To run the PyQt interface:

Navigate to the project directory:
cd /path/to/project
Run the PyQt version of the application:
python pyqt_school_management_system.py
The PyQt GUI allows you to:

Add students, instructors, and courses using structured forms
View, edit, and delete records in a table layout
Register students for courses and assign instructors
Search for records by name, ID, or course
Export records to CSV files
Save and load data from a file (pickled data)
Update dropdown menus dynamically as new data is added

Usage Instructions:

Adding Students:
In both interfaces, navigate to the Student Form.
Enter the student's name, email, and ID.
Click Add Student to save the student details.
The student will be listed in the table, and their name will be available in the dropdown for course registration.

Adding Instructors:
Navigate to the Instructor Form.
Enter the instructor's name, email, and ID.
Click Add Instructor to save the instructor's details.
The instructor will be listed in the table, and their name will be available in the dropdown for course assignment.

Adding Courses:
Navigate to the Course Form.
Enter the course name and ID.
Click Add Course to save the course.
The course will appear in the table and in the dropdowns for assigning students and instructors.

Registering Students for Courses:
Select the student and course from the dropdown menus in the Register Student for Course section.
Click Register to enroll the student in the course.

Assigning Instructors to Courses:
Select the instructor and course from the dropdown menus in the Assign Instructor to Course section.
Click Assign to assign the instructor to the course.

Saving and Loading Data:
Use the Save Data button to save the current records (students, instructors, courses) to a file.
Use the Load Data button to load previously saved records.

Exporting to CSV:
Click the Export to CSV button to save all records to a CSV file.

If you have any questions or issues, please feel free to reach out via email at:
rendchamas@gmail.com
khazenjenny@gmail.com
