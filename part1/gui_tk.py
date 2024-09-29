
"""
School Management System

This module represents the main interface of the School Management System built using the Tkinter framework.
It allows users to interact with students, instructors, and courses within the system.

Imports:
    - tkinter: Standard Python library for GUI development.
    - tkinter.ttk: Module providing themed widgets for Tkinter.
    - part1.classes: Contains the class definitions for `Student`, `Instructor`, and `Course`.
    - time: Standard Python library for time-related functions.
    - data_management: Module for handling data persistence and management.
    - tkinter.messagebox: Provides message box functions such as `showinfo` and `askyesno`.
    - pickle: Standard Python library for serializing and deserializing Python objects.
    - os: Standard Python library for interacting with the operating system.

Classes: 
    - Person: This is a conceptual class representation of a person
    - Student: This is a conceptual class representation of a student, which inherits from the :class:`Person` class
    - Instructor: This is a conceptual class representation of an instructor, which inherits from the :class:`Person` class
    - Course: This is a conceptual class representation of a course.
    
Global Variables:
    - available_courses (list): A list of available courses in the system.
    - students (list): A list of students in the system.
    - instructors (list): A list of instructors in the system.
    
    - student_columns (tuple): Columns for the student Treeview, containing student_id, name, and age.
    - student_tree (ttk.Treeview): Treeview for displaying student information.
    
    - instructor_columns (tuple): Columns for the instructor Treeview, containing instructor_id, name, and age.
    - instructor_tree (ttk.Treeview): Treeview for displaying instructor information.
   
    - course_columns (tuple): Columns for the course Treeview, containing course_id, course_name, and instructor.
    - course_tree (ttk.Treeview): Treeview for displaying course information.
    
    - items (list): A list to keep track of various items related to students, instructors, and courses.

    - search_entry(tk.Entry): Entry widget for the user to input search queries.
    - search_button (tk.Button): Button to initiate the search. When clicked, it calls the `search_all` function, which searches for students, instructors, and courses based on the input in `search_entry`.
    - student_tree.bind: Binds the `<<TreeviewSelect>>` event to the `item_selected` function for the `student_tree`. When a student is selected, their information is displayed.
    - instructor_tree.bind: Binds the `<<TreeviewSelect>>` event to the `item_selected` function for the `instructor_tree`. When an instructor is selected, their information is displayed.
    - course_tree.bind: Binds the `<<TreeviewSelect>>` event to the `item_selected` function for the `course_tree`. When a course is selected, its information is displayed.
    
Functions:

    - populate_tree(): Clears and populates the Treeview tables for students, instructors, and courses.
    - item_selected(event, tree_type): Displays information about the selected item in the specified Treeview (students, instructors, or courses).
    - search_students(): Searches for students based on the input from the search entry field.
    - search_instructors(): Searches for instructors based on the input from the search entry field.
    - search_courses(): Searches for courses based on the input from the search entry field.
    - search_all(): Searches for students, instructors and courses based on the input from the search entry field.

    - open_student_form(): Opens a new window for adding a student to the system. The form collects the student's details such as name, email, student ID, and allows the selection of a course.
    - open_instructor_form(): Opens a new window for adding a instructor to the system. The form collects the instructor's details such as name, age, email, instructor ID, and allows the selection of a course.
    - open_course_form(): Opens a new window for adding a course to the system. The form collects the course's details specifically the course name and course ID.
    
    - edit_student():  Allows the user to edit or delete the details of a selected student from the Treeview. Opens a new window to modify the student's name, age, and student ID.
    - edit_instructor(): Allows the user to edit or delete the details of a selected instructor.
    - edit_course(): Allows the user to edit or delete the details of a selected course.

    - save_data(students, instructors, courses, file_name="school_data.pkl"): Serializes and saves the student, instructor, and course data to a specified file using the `pickle` module.
    - load_data(file_name="school_data.pkl): Loads previously saved student, instructor, and course data from a specified file using the `pickle` module.
    - savedata(): Wrapper function that calls `save_data()` with the current global variables `students`, `instructors`, `available_courses` to save them to the default file "school_data.pkl".
    - loaddata():  Wrapper function that calls `load_data()` to load data from the default file "school_data.pkl" and update the system's global variables with the loaded data.

Buttons:

    1. "Add Student" button:
        - Command: `open_student_form()`
        - Description: Opens the form for adding a new student.
        - Position: Grid row 2, column 0, spans the entire width of the column.

    2. "Add Instructor" button:
        - Command: `open_instructor_form()`
        - Description: Opens the form for adding a new instructor.
        - Position: Grid row 2, column 1.

    3. "Add Course" button:
        - Command: `open_course_form()`
        - Description: Opens the form for adding a new course.
        - Position: Grid row 2, column 2.

    4. "Assign Course to Instructor" button:
        - Command: `assign_courses()`
        - Description: Opens the form to assign a course to an instructor.
        - Position: Grid row 3, column 1.

    5. "Enroll Student to Course" button:
        - Command: `enroll_students()`
        - Description: Opens the form to enroll a student in a course.
        - Position: Grid row 3, column 0.

    6. "Edit Student record" button:
        - Command: `edit_student()`
        - Description: Opens the form to edit a selected student’s record.
        - Position: Grid row 4, column 0.

    7. "Edit Instructor record" button:
        - Command: `edit_instructor()`
        - De

"""

import tkinter as tk
from tkinter import ttk
from part1.classes import *
import time
from data_management import *
from tkinter.messagebox import showinfo, askyesno
import pickle 
import os 
from data_validation import *

class Person:
    """This is a conceptual class representation of a person.
    
    :param name: name of the person
    :type name: str
    :param age: age of the person
    :type age: int
    :param email: The email address of the person
    :type email: str
    
    :raises ValueError: If any of the parameters fail validation
    """
    def __init__(self, name, age, email):
        """Constructor method
        """
        validate_string(name, 'name')
        validate_age(age)
        validate_email(email)
        
        self.name = name
        self.age = age
        self._email = email
   
    def introduce(self):
        """Introduces the person
        :returns: A string introducing the person with their name and age
        :rtype: str"""
        
        return f"My name is {self.name}, and I am {self.age} years old."

    def to_dict(self):
        """Converts person's info to a dictionary
        
        :returns: Dictionary containing the person's name, age and email
        :rtype: dict"""
        return {
            'name': self.name,
            'age': self.age,
            '_email': self._email
        }

    @classmethod
    def from_dict(cls, data):
        
        """Creates a Person instance from a dictionary
        :param data: A dictionary containing a person's details
        :type data: dict
        :returns: a Person instance with attributes from the dictionary
        :rtype: Person"""
        
        return cls(data['name'], data['age'], data['_email'])
   
class Student(Person):
    """This is a conceptual class representation of a student, which inherits from the :class:`Person` class
    
    :param name: Name of student
    :type name: str
    :param age: Age of student
    :type age: int
    :param email: Email address of student
    :type email: str
    :param student_id: Unique ID of the student 
    :type student_id: str
    
    :raises ValueError: If any of the parameters fail validation or if an invalid Course object is passed to register
    """
    
    def __init__(self, name, age, email, student_id):
        """
        Constructor method
        """
        super().__init__(name, age, email)
        
        validate_string(student_id, 'student_id')
        self.student_id = student_id
        self.registered_courses = []
        
    def register_courses(self, course):
        """Registers the student for a course

        
        :param course: course to be registered, which must be a valid :class:`Course`.
        :type course: Course
        
        :raises  ValueError: If the course is not an instance of the :class:`Course`.
        """
        
        if not isinstance(course, Course):
            raise ValueError("Invalid course")
        
        self.registered_courses.append(course)

    def __str__(self):
        """
        Returns the student's ID as a string.

        :returns: The student ID
        :rtype: str
        """
        return self.student_id
        
    def to_dict(self):
        """
        Converts the student's details to a dictionary format, including registered courses.

        :returns: A dictionary containing the student's details and registered courses.
        :rtype: dict
        """
        return {
            **super().to_dict(),
            'student_id': self.student_id,
            'registered_courses': [course.to_dict() for course in self.registered_courses]
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Student instance from a dictionary.

        :param data: A dictionary containing the student's details
        :type data: dict
        :returns: A Student instance with the provided attributes.
        :rtype: Student
        """
        student = cls(data['student_id'], data['name'], data['age'], data['_email'])
        student.registered_courses = [Course.from_dict(course_data) for course_data in data['registered_courses']]
        return student
    
    def print(self):
        """
        Prints the student's details, including name, age, and student ID.
        """
        print(f"{self.name}, {self.age}, {self.student_id}")

class Instructor(Person):
    """
    This is a conceptual class representation of an instructor, which inherits from the :class:`Person` class.

    :param name: The name of the instructor
    :type name: str
    :param age: The age of the instructor
    :type age: int
    :param email: The email address of the instructor
    :type email: str
    :param instructor_id: The unique instructor ID
    :type instructor_id: str

    :raises ValueError: If any parameters fail validation or if an invalid course is assigned.
"""
    def __init__(self, name, age, email, instructor_id):
        """Constructor method"""
        super().__init__(name, age, email)
        
        validate_string(instructor_id, 'instructor id')
        self.instructor_id = instructor_id
        self.assigned_courses = []
        
    def assign_course(self, course):
        """
        Assigns a course to the instructor.

        :param course: The course to be assigned, which must be a valid :class:`Course`.
        :type course: Course
        :raises ValueError: If the course is not an instance of the :class:`Course` class.
        """
        
        if not isinstance(course, Course):
            raise ValueError("Invalid course")
        
        self.assigned_courses.append(course)
        
    def __str__(self):
        """
        Returns the instructor's ID as a string.

        :returns: The instructor ID
        :rtype: str
        """
        return self.instructor_id
        
    def to_dict(self):
        """
        Converts the instructor's details to a dictionary format, including assigned courses.

        :returns: A dictionary containing the instructor's details and assigned courses.
        :rtype: dict
        """
        return {
            **super().to_dict(),
            'instructor_id': self.instructor_id,
            'assigned_courses': [course.to_dict() for course in self.assigned_courses]
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates an Instructor instance from a dictionary.

        :param data: A dictionary containing the instructor's details
        :type data: dict
        :returns: An Instructor instance with the provided attributes.
        :rtype: Instructor
        """
        instructor = cls(data['instructor_id'], data['name'], data['age'], data['_email'])
        instructor.assigned_courses = [Course.from_dict(course_data) for course_data in data['assigned_courses']]
        return instructor

class Course:
    """
    This is a conceptual class representation of a course.

    :param course_id: The unique course ID
    :type course_id: str
    :param course_name: The name of the course
    :type course_name: str
    :param instructor: The instructor teaching the course, defaults to None
    :type instructor: Instructor, optional

    :raises ValueError: If any parameters fail validation or if an invalid student/instructor is added.
"""
    def __init__(self, course_id, course_name, instructor=None):
        """Constructor method"""
        validate_string(course_id, 'course id')
        validate_string(course_name, 'course name')
        
        self.course_id = course_id
        self.course_name = course_name
        self.instructor = instructor
        self.enrolled_students = []
        
    def add_student(self, student):
        """Adds a student to the course.

        :param student: The student to enroll in the course, must be a valid :class:`Student`.
        :type student: Student
        :raises ValueError: If the student is not an instance of the :class:`Student` class.
        """
        if not isinstance(student, Student):
           raise ValueError("Invalid student")
       
        self.enrolled_students.append(student) 
        
    def add_instructor(self, instructor):
        """
        Assigns an instructor to the course.

        :param instructor: The instructor to be assigned to the course, must be a valid :class:`Instructor`.
        :type instructor: Instructor
        :raises ValueError: If the instructor is not an instance of the :class:`Instructor` class.
        """
        if not isinstance(instructor, Instructor):
           raise ValueError("Invalid instructor")
       
        self.instructor = instructor
        
    def __str__(self):
        """
        Returns the course name as a string.

        :returns: The course name
        :rtype: str
        """
        return self.course_name
    
    def __repr__(self):
        """
        Returns a detailed string representation of the course.

        :returns: A string representation of the course object
        :rtype: str
        """
        return f"Course({self.course_name})"  
        
    def to_dict(self):
        """
        Converts the course's details to a dictionary format, including the instructor and enrolled students.

        :returns: A dictionary containing the course's details, instructor, and enrolled students.
        :rtype: dict
        """
        return {
            'course_id': self.course_id,
            'course_name': self.course_name,
            'instructor': self.instructor.to_dict() if self.instructor else None,
            'enrolled_students': [student.to_dict() for student in self.enrolled_students]
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Course instance from a dictionary.

        :param data: A dictionary containing the course's details
        :type data: dict
        :returns: A Course instance with the provided attributes
        :rtype: Course
        """
        instructor = Instructor.from_dict(data['instructor']) if data['instructor'] else None
        course = cls(data['course_id'], data['course_name'], instructor)
        course.enrolled_students = [Student.from_dict(student_data) for student_data in data['enrolled_students']]
        return course
        
#Main Window
root = tk.Tk()
root.title("School Management System")

#Keep track of everything
available_courses = []
students = []
instructors = []

#Student Treeviews
student_columns = ('student_id', 'name', 'age')
student_tree = ttk.Treeview(root, columns=student_columns, show="headings")

student_tree.heading('student_id', text="Student ID")
student_tree.heading('name', text="Name")
student_tree.heading('age', text="Age")

student_tree.column('student_id', width=100)
student_tree.column('name', width=100)
student_tree.column('age', width=100)

#Instructor Treeviews
instructor_columns = ('instructor_id', 'name', 'age')
instructor_tree = ttk.Treeview(root, columns=instructor_columns, show="headings")

instructor_tree.heading('instructor_id', text="Instructor ID")
instructor_tree.heading('name', text="Name")
instructor_tree.heading('age', text="Age")

instructor_tree.column('instructor_id', width=100)
instructor_tree.column('name', width=100)
instructor_tree.column('age', width=100)

#Course Treeviews
course_columns = ('course_id', 'course_name', 'instructor')
course_tree = ttk.Treeview(root, columns=course_columns, show='headings')

course_tree.heading('course_id', text="Course ID")
course_tree.heading('course_name', text="Course Name")
course_tree.heading('instructor', text="Instructor")

course_tree.column('course_id', width=100)
course_tree.column('course_name', width=100)
course_tree.column('instructor', width=100)

#List of items
items = []

def populate_tree():
    
    """
    Populates the Treeview tables for students, instructors, and courses 
    in the School Management System.

    This function first clears all existing entries in the student, 
    instructor, and course Treeviews. It then populates the student Treeview 
    with the current list of students, the instructor Treeview with the 
    current list of instructors, and the course Treeview with the available 
    courses, including the instructor's name if assigned.

    Steps:
        1. Clear all entries in the student, instructor, and course Treeviews.
        2. Insert each student into the student Treeview, displaying their 
           student ID, name, and age.
        3. Insert each instructor into the instructor Treeview, displaying 
           their instructor ID, name, and age.
        4. Insert each course into the course Treeview, displaying the 
           course ID, course name, and the name of the assigned instructor 
           (if available).
    
    Returns:
        None
    """
    
    #clear tables before populating
    for tree in [student_tree, instructor_tree, course_tree]:
        for row in tree.get_children():
            tree.delete(row)
            
    #populate students
    for student in students:
        student_tree.insert('', tk.END, values = (student.student_id,student.name, student.age))
    
    for instructor in instructors:
        instructor_tree.insert('', tk.END, values=(instructor.instructor_id, instructor.name, instructor.age))
        
    for course in available_courses:
        instructor_name = course.instructor.name if course.instructor else None
        course_tree.insert('', tk.END, values=(course.course_id, course.course_name, instructor_name))


def item_selected(event, tree_type):
    """
    Displays information about the selected item in the specified Treeview.

    This function is triggered when an item in a Treeview is selected. It checks
    the type of Treeview (students, instructors, or courses) and retrieves the 
    relevant information from the selected item. A message box is then shown 
    displaying detailed information about the selected student, instructor, 
    or course.

    Parameters:
        event (tk.Event): The event object representing the selection event.
        tree_type (ttk.Treeview): The Treeview from which the item was selected, 
                                   can be one of student_tree, instructor_tree, 
                                   or course_tree.

    Returns:
        None
    """
    selected_items = tree_type.selection()
    
    if not selected_items:
        return 
    
    selected_item = selected_items[0]
    record = tree_type.item(selected_item, 'values')
    
    if tree_type == student_tree:
        student_value = record[0]
        selected_student=next((student for student in students if student.student_id == student_value), None)
        
        if selected_student:
            info = f"Student ID: {selected_student.student_id}\nName: {selected_student.name}\nAge: {selected_student.age}"
            showinfo(title="Student Information", message=info)  
    
    elif tree_type == instructor_tree:
        instructor_value = record[0]
        selected_instructor = next((instructor for instructor in instructors if instructor.instructor_id == instructor_value), None)
        if selected_instructor:
            info = f"Instructor ID: {selected_instructor.instructor_id}\nName: {selected_instructor.name}\nAge: {selected_instructor.age}"
            showinfo(title="Instructor Information", message=info)
            
    elif tree_type == course_tree:
        course_value = record[1]
        selected_course = next((course for course in available_courses if course.course_name == course_value), None)
        if selected_course:
            info = f"Course ID: {selected_course.course_id}\nCourse Name: {selected_course.course_name}\nInstructor: {selected_course.instructor.name if selected_course.instructor else 'None'}"
            showinfo(title="Course Information", message=info)
    
def search_students():
    """
    Searches for students based on the input from the search entry field.

    This function retrieves the search term entered by the user, clears the current
    entries in the student Treeview, and populates it with students whose
    student ID or name matches the search term (case insensitive).

    Returns:
        None
    """
    search_term = search_entry.get().lower()

    # Clear the tree before displaying new search results
    for row in student_tree.get_children():
        student_tree.delete(row)

    # Search through the students list
    for student in students:
        if (search_term in student.student_id.lower() or
            search_term in student.name.lower()):
            student_tree.insert('', tk.END, values=(student.student_id, student.name, student.age))

def search_instructors():
    """
    Searches for instructors based on the input from the search entry field.

    This function retrieves the search term entered by the user, clears the current
    entries in the instructor Treeview, and populates it with instructors whose
    instructor ID or name matches the search term (case insensitive).

    Returns:
        None
    """
    search_term = search_entry.get().lower()

    # Clear the tree before displaying new search results
    for row in instructor_tree.get_children():
        instructor_tree.delete(row)

    # Search through the instructors list
    for instructor in instructors:
        if (search_term in instructor.instructor_id.lower() or
            search_term in instructor.name.lower()):
            instructor_tree.insert('', tk.END, values=(instructor.instructor_id, instructor.name, instructor.age))

def search_courses():
    """
    Searches for courses based on the input from the search entry field.

    This function retrieves the search term entered by the user, clears the current
    entries in the courses Treeview, and populates it with courses whose
    course ID or course name matches the search term (case insensitive).

    Returns:
        None
    """
    search_term = search_entry.get().lower()

    # Clear the tree before displaying new search results
    for row in course_tree.get_children():
        course_tree.delete(row)

    # Search through the available courses list
    for course in available_courses:
        if (search_term in course.course_id.lower() or
            search_term in course.course_name.lower()):
            course_tree.insert('', tk.END, values=(course.course_id, course.course_name))
                      
def search_all():
    """
    Searches for students, instructors, and courses based on user input.

    This function calls the `search_students`, `search_instructors`, and 
    `search_courses` functions to update their respective Treeviews with 
    the results based on the search criteria entered by the user.

    Returns:
        None
    """
    search_students()
    search_instructors()
    search_courses()

# Create the search entry widget
search_entry = tk.Entry(root)

# Place it on the window (you can adjust the row/column values based on your layout)
search_entry.grid(row=1, column=0, columnspan=2, sticky='ew')

# Create the search button
search_button = tk.Button(root, text="Search", command=search_all)  # search_all is the combined function I mentioned earlier
search_button.grid(row=1, column=2, sticky='ew')

# Bind select event to each tree
student_tree.bind('<<TreeviewSelect>>', lambda event: item_selected(event, student_tree))
instructor_tree.bind('<<TreeviewSelect>>', lambda event: item_selected(event, instructor_tree))
course_tree.bind('<<TreeviewSelect>>', lambda event: item_selected(event, course_tree))

# Grid layout for tables
student_tree.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
instructor_tree.grid(row=0, column=1, padx=10, pady=10, sticky='nsew')
course_tree.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

"""
Layout:

    - search_entry.grid: Places the search entry field at row 1, column 0, and spans across 2 columns. It is sticky in the east-west direction, ensuring it stretches across the allocated space.
    
    - search_button.grid: Places the search button next to the search entry, at row 1, column 2. It is also sticky in the east-west direction.
    
    - student_tree.grid: Places the `student_tree` at row 0, column 0, with padding and a sticky 'nsew' configuration to ensure it stretches as the window resizes.

    - instructor_tree.grid: Places the `instructor_tree` at row 0, column 1, with padding and a sticky 'nsew' configuration.

    - course_tree.grid: Places the `course_tree` at row 0, column 2, with padding and a sticky 'nsew' configuration.
"""

#open_student_form: create student, add course
def open_student_form():
    """
Function: open_student_form()

    Opens a new window for adding a student to the system. The form collects the student's details such as name, age, email, student ID, and allows the selection of a course. 

Components:
    - student_form (tk.Toplevel): A new window (Toplevel) for adding student information.
    
    - name_entry (tk.Entry): Entry widget for the student's name.
    
    - age_entry (tk.Entry): Entry widget for the student's age.
    
    - email_entry (tk.Entry): Entry widget for the student's email.
    
    - studentid_entry (tk.Entry): Entry widget for the student's ID.
    
    - course_combobox (ttk.Combobox): A dropdown (Combobox) that allows the user to select a course from the `available_courses` list.

    - selected_courses (list): A list to store the courses selected by the user for the student.

Inner Functions:
    - add_course(student): Adds the selected course to the student's list of enrolled courses. 
        - Parameters:
            - student (Student): The `Student` object to which the course will be added.
        - Functionality:
            - Retrieves the selected course name from `course_combobox`.
            - Finds the corresponding course object from the `available_courses` list.
            - Adds the course to the student's enrolled courses if it's not already added.
            - If the course is already added, it prevents adding duplicates.

    - add_student(): Creates a new `Student` object based on the input from the form, adds the student to the global `students` list, and adds the selected course to the student's enrolled courses.
        - Functionality:
            - Collects input from `name_entry`, `age_entry`, `email_entry`, and `studentid_entry`.
            - Ensures all required fields are filled.
            - Creates a new `Student` object.
            - Appends the student to the `students` list.
            - Calls `populate_tree()` to update the Treeview display of students.
            - Calls `add_course()` to add the selected course to the student's enrolled courses.

    - exit(): Closes the student form window.
        - Functionality:
            - Destroys the `student_form` window using `student_form.destroy()`.

Buttons:
    - "Add Student" Button: Triggers the `add_student()` function to create the student and add the selected course.
    
    - "Done" Button: Closes the form window when finished by calling the `exit()` function.
"""

    student_form = tk.Toplevel(root)
    student_form.title("Add Student")
    
    tk.Label(student_form, text = "Name: ").pack()
    name_entry = tk.Entry(student_form)
    name_entry.pack()
    
    tk.Label(student_form, text = "Age: ").pack()
    age_entry = tk.Entry(student_form)
    age_entry.pack()
        
    tk.Label(student_form, text = "Email: ").pack()
    email_entry = tk.Entry(student_form)
    email_entry.pack()
    
    tk.Label(student_form, text="Student ID: ").pack()
    studentid_entry = tk.Entry(student_form)
    studentid_entry.pack()
    
    # Dropdown for available courses
    tk.Label(student_form, text="Select Course: ").pack()
    course_combobox = ttk.Combobox(student_form, values=available_courses)
    course_combobox.pack()
    
    selected_courses = []
    
    def add_course(student):
        #STRING
        selected_course_name = course_combobox.get() 
        
        #OBJECT
        selected_course = next((course for course in available_courses if course.course_name == selected_course_name), None)
       
        if selected_course and selected_course not in selected_courses:
            selected_courses.append(selected_course)
            print(f"Added course: {selected_course_name}") #Adding student to enrolled_students

            selected_course.add_student(student)
        else: 
            print("Course already added")
            
    def add_student():
        name = name_entry.get()
        age = int(age_entry.get())
        email = email_entry.get()
        student_id = studentid_entry.get()
        
        if not name or not age or not email or not student_id:
            print("PLEASE FILL EVERYTHING")
            return
        
        student = Student(name, age, email, student_id)
        print(f"Student {student.name} created")
        students.append(student)
        #tree.insert('',tk.END, values=(student_id, "", ""))
        populate_tree()
        add_course(student)
        
        
    tk.Button(student_form, text="Add Student", command=add_student).pack()
    #tk.Button(student_form, text="Add Course", command=add_course).pack()
    
    def exit():
        student_form.destroy()
        
    tk.Button(student_form, text="Done", command=exit).pack()

#open_instructor_form: create instructor, assign course
def open_instructor_form():
    """
Function: open_student_form()

    Opens a new window for adding an instructor to the system. The form collects the instructor's details such as name, age, email, instructor ID, and allows the selection of a course. 

Components:
    - instructor_form (tk.Toplevel): A new window (Toplevel) for adding student information.
    
    - name_entry (tk.Entry): Entry widget for the student's name.
    
    - age_entry (tk.Entry): Entry widget for the student's age.
    
    - email_entry (tk.Entry): Entry widget for the student's email.
    
    - instructorid_entry (tk.Entry): Entry widget for the instructor's ID.
    
    - course_combobox (ttk.Combobox): A dropdown (Combobox) that allows the user to select a course from the `available_courses` list.

    - selected_courses (list): A list to store the courses selected by the user for the instructor.

Inner Functions:
    - assign_course(student): Assigns the instructor to the selected course. 
        - Parameters:
            - instructor (Instructor): The `Instructor` object to which the course will be assigned.
        - Functionality:
            - Retrieves the selected course name from `course_combobox`.
            - Finds the corresponding course object from the `available_courses` list.
            - Adds the course to the instructor's assigned courses if it's not already added.
            - If the course is already added, it prevents adding duplicates.

    - add_instructor(): Creates a new `Instructor` object based on the input from the form, adds the instructor to the global `instructors` list, and adds the selected course to the instructors's assigned courses.
        - Functionality:
            - Collects input from `name_entry`, `age_entry`, `email_entry`, and `instructorid_entry`.
            - Ensures all required fields are filled.
            - Creates a new `Instructor` object.
            - Appends the instructor to the `instructor` list.
            - Calls `populate_tree()` to update the Treeview display of instructors.
            - Calls `assign_course()` to add the selected course to the instructor's assigned courses.

    - exit(): Closes the student form window.
        - Functionality:
            - Destroys the `instructor_form` window using `instructor_form.destroy()`.

Buttons:
    - "Add Instructor" Button: Triggers the `add_instructor()` function to create the instructor and assign the selected course.
    
    - "Done" Button: Closes the form window when finished by calling the `exit()` function.
"""
    instructor_form = tk.Toplevel(root)
    instructor_form.title("Add Student")
    
    tk.Label(instructor_form, text = "Name: ").pack()
    name_entry = tk.Entry(instructor_form)
    name_entry.pack()
    
    tk.Label(instructor_form, text = "Age: ").pack()
    age_entry = tk.Entry(instructor_form)
    age_entry.pack()
    
    tk.Label(instructor_form, text="Email: ").pack()
    email_entry = tk.Entry(instructor_form)
    email_entry.pack()
    
    tk.Label(instructor_form, text="Instructor ID: ").pack()
    instructorid_entry = tk.Entry(instructor_form)
    instructorid_entry.pack()
    
    # Dropdown for available courses
    tk.Label(instructor_form, text="Select Course: ").pack()
    course_combobox = ttk.Combobox(instructor_form, values=available_courses)
    course_combobox.pack()

    selected_courses = []
    def assign_course(instructor):
        #STRING
        selected_course_name = course_combobox.get()
        
        #OBJECT
        selected_course = next((course for course in available_courses if course.course_name == selected_course_name), None)
        
        if selected_course and selected_course not in selected_courses:
            selected_courses.append(selected_course)
            print(f"{selected_course} assigned")
            selected_course.add_instructor(instructor)
            
        else:
            print(f"{selected_course} already assigned")
        
    
    def add_instructor():
        name = name_entry.get()
        age = int(age_entry.get())
        email = email_entry.get()
        instructor_id = instructorid_entry.get()
        
        if not name or not age or not email or not instructor_id:
            print("PLEASE FILL EVERYTHING")
            return
        
        instructor = Instructor(name, age, email, instructor_id)
        instructors.append(instructor)
        print(f"Instructor {instructor.name} created")
        populate_tree()
       # tree.insert('',tk.END, values=("", instructor_id,""))
        assign_course(instructor)
        
    tk.Button(instructor_form, text="Add Instructor", command=add_instructor).pack()
   # tk.Button(instructor_form, text="Add Course", command=assign_course).pack()
    
    def exit():
        instructor_form.destroy()
        
    tk.Button(instructor_form, text="Done", command=exit).pack()
       
#open_course_form: add course
def open_course_form(): 
    """Opens a new window to allow the user to create a Course object, by inputting the course name and course id.

Components:
    - course_form (tk.Toplevel): A new window (Toplevel) for adding course information.
    
    - courseid_entry (tk.Entry): Entry widget for the course's id.
    
    - coursename_entry (tk.Entry): Entry widget for the course's name.
    
Inner Functions:
    - add_course(): Creates a new `Course` object based on the input from the form, adds course to the global `available_courses` list.
        - Functionality:
            - Collects input from `coursename_entry` and `courseid_entry`.
            - Ensures all required fields are filled.  
            - Creates a new `Course` object.
            - Appends the instructor to the `available_courses` list.
            - Calls `populate_tree()` to update the Treeview display of courses.

    - exit(): Closes the student form window.
        - Functionality:
            - Destroys the `course_form` window using `course_form.destroy()`.
            
Buttons:
    - "Add Course" Button: Triggers the `add_course()` function to create the course.
    
    - "Done" Button: Closes the form window when finished by calling the `exit()` function.

    """
    course_form = tk.Toplevel(root)
    course_form.title("Add Student")
    
    tk.Label(course_form, text = "Course ID: ").pack()
    courseid_entry = tk.Entry(course_form)
    courseid_entry.pack()
    
    tk.Label(course_form, text = "Course Name: ").pack()
    coursename_entry = tk.Entry(course_form)
    coursename_entry.pack()
    
    def add_course():
        courseid = courseid_entry.get()
        coursename = coursename_entry.get()
        
        if not courseid or not coursename:
            print("PLEASE FILL EVERYTHING")
            return
        
        course = Course(courseid, coursename)
        available_courses.append(course)
        
        populate_tree()
        
    def exit():
        course_form.destroy()
        
    tk.Button(course_form, text="Add Course", command=add_course).pack()
    tk.Button(course_form, text="Done", command=exit).pack()
    

def assign_courses():
    assign_form = tk.Toplevel(root)
    assign_form.title("Assign Course")
    
    #Dropdown for selecting a course
    tk.Label(assign_form, text="Select Course: ").pack()
    course_combobox = ttk.Combobox(assign_form, values=available_courses)
    course_combobox.pack()

    
    #Dropdown for selecting an instructor
    tk.Label(assign_form, text = "Select Instructor: ").pack()
    instructor_combobox = ttk.Combobox(assign_form, values=instructors)
    instructor_combobox.pack()

    
    def assign():
        selected_course_name = course_combobox.get()
        selected_instructor_id = instructor_combobox.get()
        
        print(f"Selected course: {selected_course_name}")
        print(f"Selected instructor: {selected_instructor_id}")
        
        if not selected_course_name or not selected_instructor_id:
            print("PLEASE PRINT EVERYTHING")
            return
        
        selected_course = next((course for course in available_courses if course.course_name == selected_course_name), None)
        selected_instructor = next((instr for instr in instructors if instr.instructor_id == selected_instructor_id), None)
        
        if selected_course and selected_instructor:
            selected_course.add_instructor(selected_instructor)
            selected_instructor.assign_course(selected_course)
            print(f"{selected_course} assigned to {selected_instructor} and vice versa")
            populate_tree()
            
        else:
            print("Invalid selection")
            
    tk.Button(assign_form, text="Assign Course", command=assign).pack()
        
    def exit_form(): 
        assign_form.destroy()
        
    tk.Button(assign_form, text="Close", command=exit_form).pack()
        

def enroll_students():
    enroll_form = tk.Toplevel(root)
    enroll_form.title("Enroll Student")
    
      #Dropdown for selecting a course
    tk.Label(enroll_form, text="Select Course: ").pack()
    course_combobox = ttk.Combobox(enroll_form, values=available_courses)
    course_combobox.pack()

    
    #Dropdown for selecting an instructor
    tk.Label(enroll_form, text = "Select Instructor: ").pack()
    student_combobox = ttk.Combobox(enroll_form, values=students)
    student_combobox.pack()
    
    def enroll():
        selected_course_name = course_combobox.get()
        selected_student_id = student_combobox.get()
        
        print(f"Selected course: {selected_course_name}")
        print(f"Selected instructor: {selected_student_id}")
        
        if not selected_course_name or not selected_student_id:
            print("PLEASE PRINT EVERYTHING")
            return
        
        selected_course = next((course for course in available_courses if course.course_name == selected_course_name), None)
        selected_student = next((student for student in students if student.student_id == selected_student_id), None)
        
        if selected_course and selected_student:
            selected_course.add_student(selected_student)
            selected_student.register_courses(selected_course)
            print(f"{selected_course} registered for {selected_student} and vice versa")
            populate_tree()
            
        else:
            print("Invalid selection")
            
    tk.Button(enroll_form, text="Assign Course", command=enroll).pack()
        
    def exit_form(): 
        enroll_form.destroy()
        
    tk.Button(enroll_form, text="Close", command=exit_form).pack()

def edit_student():
    selected_items = student_tree.selection()
    if not selected_items:
        showinfo(title="Error", message="Please select a student to edit.")
        return
    
    selected_item = selected_items[0]
    record = student_tree.item(selected_item, 'values')
    selected_student_id = record[0]
    
    selected_student = next((student for student in students if student.student_id == selected_student_id), None)

    if not selected_student:
        showinfo(title="Error", message="Student not found.")
        return
    
    edit_form = tk.Toplevel(root)
    edit_form.title("Edit Student")
    
    tk.Label(edit_form, text="Name: ").pack()
    name_entry = tk.Entry(edit_form)
    name_entry.insert(0, selected_student.name)
    name_entry.pack()
    
    tk.Label(edit_form, text="Age: ").pack()
    age_entry = tk.Entry(edit_form)
    age_entry.insert(0, str(selected_student.age))
    age_entry.pack()
    
    tk.Label(edit_form, text="Student ID: ").pack()
    studentid_entry = tk.Entry(edit_form)
    studentid_entry.insert(0, selected_student.student_id)
    studentid_entry.pack()
    
    def save_changes():
        selected_student.name = name_entry.get()
        selected_student.age = int(age_entry.get())
        selected_student.student_id = studentid_entry.get()
        
        populate_tree() 
        edit_form.destroy()
        
    def delete():
        confirm = askyesno(title="Confirm Delete", message=f"Are you sure you want to delete student with ID {selected_student_id}?")
        if not confirm:
            return
        
        global students
        students = [student for student in students if student.student_id != selected_student_id]
    
        populate_tree()
        showinfo(title="Success", message="Student deleted successfully!")

        
    
    tk.Button(edit_form, text="Save Changes", command=save_changes).pack()
    tk.Button(edit_form, text="Delete", command=delete).pack()
    
def edit_instructor():
    """
Function: edit_instructor()

    Allows the user to edit or delete the details of a selected instructor from the Treeview. Opens a new window to modify the instructor's name, age, and instructor ID.

Components:
    - selected_items (list): List of selected items from the `instructor_tree`. Should contain the ID of the instructor selected for editing.
    
    - selected_instructor (Instructor): The `Instructor` object corresponding to the selected instructor's ID. Retrieved from the global `instructors` list.

    - edit_form (tk.Toplevel): A new window for editing instructor details.

    - name_entry (tk.Entry): Entry widget pre-filled with the instructor's current name for editing.
    
    - age_entry (tk.Entry): Entry widget pre-filled with the instructor's current age for editing.
    
    - studentid_entry (tk.Entry): Entry widget pre-filled with the instructor's current instructor ID for editing.

Inner Functions:
    - save_changes(): Saves the updated instructor details and closes the edit window.
        - Functionality:
            - Updates the `name`, `age`, and `instructor_id` fields of the selected `Instructor` object.
            - Calls `populate_tree()` to refresh the Treeview display with the updated instructor information.
            - Closes the `edit_form` after saving changes.
    
    - delete(): Deletes the selected instructor from the system.
        - Functionality:
            - Confirms with the user whether they want to proceed with deleting the instructor.
            - If confirmed, removes the instructor from the `instructors` list.
            - Calls `populate_tree()` to refresh the Treeview after deletion.
            - Displays a success message once the instructor is deleted.

Error Handling:
    - If no instructor is selected from the Treeview, an error message is shown to the user via `showinfo()`.
    
    - If the selected instructor ID does not match any instructor in the system, an error message is displayed via `showinfo()`.

Buttons:
    - "Save Changes" Button: Calls `save_changes()` to apply changes to the instructor's information.
    
    - "Delete" Button: Calls `delete()` to remove the instructor from the system after confirmation.
"""

    selected_items = instructor_tree.selection()
    if not selected_items:
        showinfo(title="Error", message="Please select an instructor to edit.")
        return
    
    selected_item = selected_items[0]
    record = instructor_tree.item(selected_item, 'values')
    selected_instructor_id = record[0]
    
    selected_instructor = next((instr for instr in instructors if instr.instructor_id == selected_instructor_id), None)

    if not selected_instructor:
        showinfo(title="Error", message="Instructor not found.")
        return
    
    edit_form = tk.Toplevel(root)
    edit_form.title("Edit Instructor")
    
    tk.Label(edit_form, text="Name: ").pack()
    name_entry = tk.Entry(edit_form)
    name_entry.insert(0, selected_instructor.name)
    name_entry.pack()
    
    tk.Label(edit_form, text="Age: ").pack()
    age_entry = tk.Entry(edit_form)
    age_entry.insert(0, str(selected_instructor.age))
    age_entry.pack()
    
    tk.Label(edit_form, text="Instructor ID: ").pack()
    studentid_entry = tk.Entry(edit_form)
    studentid_entry.insert(0, selected_instructor.instructor_id)
    studentid_entry.pack()
    
    def save_changes():
        selected_instructor.name = name_entry.get()
        selected_instructor.age = int(age_entry.get())
        selected_instructor.student_id = studentid_entry.get()
        
        populate_tree() 
        edit_form.destroy()
        
    def delete():
        confirm = askyesno(title="Confirm Delete", message=f"Are you sure you want to delete student with ID {selected_instructor_id}?")
        if not confirm:
            return
        
        global instructors
        instructors = [instr for instr in instructors if instr.instructor_id != selected_instructor_id]
    
        populate_tree()
        showinfo(title="Success", message="Instructor deleted successfully!")

    tk.Button(edit_form, text="Save Changes", command=save_changes).pack()
    tk.Button(edit_form, text="Delete", command=delete).pack()
   
def edit_course():
    """
Function: edit_course()

    Allows the user to edit or delete the details of a selected course from the Treeview. Opens a new window to modify the course's name and course ID.

Components:
    - selected_items (list): List of selected items from the `course_tree`. Should contain the ID of the course selected for editing.
    
    - selected_course (Course): The `Course` object corresponding to the selected course's ID. Retrieved from the global `available_courses` list.

    - edit_form (tk.Toplevel): A new window for editing course details.

    - name_entry (tk.Entry): Entry widget pre-filled with the course's current name for editing.
    
    - id_entry (tk.Entry): Entry widget pre-filled with the course's current ID for editing.

Inner Functions:
    - save_changes(): Saves the updated course details and closes the edit window.
        - Functionality:
            - Updates the `course_name` and `course_id` fields of the selected `Course` object.
            - Calls `populate_tree()` to refresh the Treeview display with the updated course information.
            - Closes the `edit_form` after saving changes.
    
    - delete(): Deletes the selected course from the system.
        - Functionality:
            - Confirms with the user whether they want to proceed with deleting the course.
            - If confirmed, removes the course from the `available_courses` list.
            - Calls `populate_tree()` to refresh the Treeview after deletion.
            - Displays a success message once the course is deleted.

Error Handling:
    - If no course is selected from the Treeview, an error message is shown to the user via `showinfo()`.
    
    - If the selected course ID does not match any course in the system, an error message is displayed via `showinfo()`.

Buttons:
    - "Save Changes" Button: Calls `save_changes()` to apply changes to the course's information.
    
    - "Delete" Button: Calls `delete()` to remove the course from the system after confirmation.
"""

    selected_items = course_tree.selection() 
    if not selected_items:
        showinfo(title="Error", message="Please select a course to edit.")
        return
    
    selected_item = selected_items[0]
    record = course_tree.item(selected_item, 'values')
    selected_course_id = record[0]
    
    selected_course = next((course for course in available_courses if course.course_id == selected_course_id), None)

    if not selected_course:
        showinfo(title="Error", message="Course not found.")
        return
    
    edit_form = tk.Toplevel(root)
    edit_form.title("Edit Course")
    
    tk.Label(edit_form, text="Course name: ").pack()
    name_entry = tk.Entry(edit_form)
    name_entry.insert(0, selected_course.course_name)
    name_entry.pack()
    
    tk.Label(edit_form, text="Course ID: ").pack()
    id_entry = tk.Entry(edit_form)
    id_entry.insert(0, str(selected_course.course_id))
    id_entry.pack()
    
    def save_changes():
        selected_course.course_name = name_entry.get()
        selected_course.course_id = id_entry.get()
        
        populate_tree() 
        edit_form.destroy()
        
    def delete():
        confirm = askyesno(title="Confirm Delete", message=f"Are you sure you want to delete course with ID {selected_course_id}?")
        if not confirm:
            return
        
        global available_courses
        available_courses = [course for course in available_courses if course.course_id != selected_course_id]
    
        populate_tree()
        showinfo(title="Success", message="Course deleted successfully!")

    tk.Button(edit_form, text="Save Changes", command=save_changes).pack()
    tk.Button(edit_form, text="Delete", command=delete).pack()

def save_data(students, instructors, courses, file_name="school_data.pkl"):
    """
Function: save_data(students, instructors, courses, file_name="school_data.pkl")

    Serializes and saves the student, instructor, and course data to a specified file using the `pickle` module.

Parameters:
    - students (list): A list containing all `Student` objects in the system.
    - instructors (list): A list containing all `Instructor` objects in the system.
    - courses (list): A list containing all `Course` objects in the system.
    - file_name (str): The name of the file where data will be saved. Default is "school_data.pkl".

Functionality:
    - The function opens the specified file in write-binary mode.
    - It creates a dictionary containing `students`, `instructors`, and `courses` and uses `pickle.dump()` to serialize and store this data.
    - Upon successful saving, a message "Data successfully saved" is printed.

Returns:
    None
    """
    
    with open(file_name, 'wb') as file:
        data = {
            "students": students,
            "instructors": instructors,
            "courses": courses
        }
        pickle.dump(data, file)
        print("Data successfully saved")
    return

def load_data(file_name="school_data.pkl"):
    """
    Function: load_data(file_name="school_data.pkl")

    Loads previously saved student, instructor, and course data from a specified file using the `pickle` module.

Parameters:
    - file_name (str): The name of the file from which to load the data. Default is "school_data.pkl".

Functionality:
    - The function first checks if the specified file exists using `os.path.exists()`.
    - If the file exists, it opens it in read-binary mode and uses `pickle.load()` to deserialize the saved data.
    - The global variables `students`, `instructors`, and `available_courses` are updated with the loaded data.
    - Calls `populate_tree()` to refresh the Treeview with the loaded data.
    - If the file does not exist, an empty list is assigned to `students`, `instructors`, and `available_courses`, and a message "No saved data found" is printed.

Returns:
    None
    """
    global students, instructors, available_courses
    
    if os.path.exists(file_name):
        with open(file_name, 'rb') as file:
            data = pickle.load(file)
            print("Data loaded successfully.")
            students = data["students"]
            instructors = data["instructors"]
            available_courses=data["courses"]
            
            populate_tree()
    else:
        print("No saved data found.")
        students, instructors, available_courses = [], [], []
 
def savedata():
    """
    Function: savedata()

    Wrapper function that calls `save_data()` with the current global variables `students`, `instructors`, and `available_courses` to save them to the default file "school_data.pkl".

Parameters:
    None

Returns:
    None
    """
    
    save_data(students, instructors, available_courses)

def loaddata():
    """
    Function: loaddata()

    Wrapper function that calls `load_data()` to load data from the default file "school_data.pkl" and update the system's global variables with the loaded data.

Parameters:
    None

Returns:
    None
"""
    load_data()


# Buttons
tk.Button(root, text="Add Student", command=open_student_form).grid(row=2, column=0, sticky='ew')
tk.Button(root, text="Add Instructor", command=open_instructor_form).grid(row=2, column=1, sticky='ew')
tk.Button(root, text="Add Course", command=open_course_form).grid(row=2, column=2, sticky='ew')

tk.Button(root, text="Assign Course to Instructor", command=assign_courses).grid(row=3, column=1, sticky='ew')
tk.Button(root, text="Enroll Student to Course", command = enroll_students).grid(row=3, column=0,sticky='ew')

tk.Button(root, text="Edit Student record", command=edit_student).grid(row=4, column=0, sticky='ew')
tk.Button(root, text="Edit Instructor record", command=edit_instructor).grid(row=4, column=1, sticky='ew')
tk.Button(root, text="Edit Course record", command=edit_course).grid(row=4, column=2, sticky='ew')
    
tk.Button(root, text="Save", command=savedata).grid(row=5, column=0, columnspan=3, sticky='ew')
tk.Button(root, text="Load", command=loaddata).grid(row=6, column=0, columnspan=3, sticky='ew')

root.mainloop()

