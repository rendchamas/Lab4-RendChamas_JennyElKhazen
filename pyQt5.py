import csv
import re
import sys
import sqlite3
import pickle
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QComboBox,
    QMessageBox,
    QGroupBox,
    QTableWidget,
    QTableWidgetItem,
    QScrollArea,
    QWidget,
)


class Student:
    """
    Represents a student in the school management system.

    Attributes:
        name (str): The name of the student.
        student_id (str): The unique identifier for the student.
        email (str): The email address of the student.
        registered_courses (list): A list of courses the student is registered in.
    """

    def __init__(self, name, student_id, email):
        """
        Initializes a new Student instance.

        Args:
            name (str): The name of the student.
            student_id (str): The unique identifier for the student.
            email (str): The email address of the student.
        """
        self.name = name
        self.student_id = student_id
        self.email = email
        self.registered_courses = []


class Instructor:
    """
    Represents an instructor in the school management system.

    Attributes:
        name (str): The name of the instructor.
        email (str): The email address of the instructor.
        instructor_id (str): The unique identifier for the instructor.
        assigned_courses (list): A list of courses the instructor is assigned to.
    """

    def __init__(self, name, email, instructor_id):
        """
        Initializes a new Instructor instance.

        Args:
            name (str): The name of the instructor.
            email (str): The email address of the instructor.
            instructor_id (str): The unique identifier for the instructor.
        """
        self.name = name
        self.email = email
        self.instructor_id = instructor_id
        self.assigned_courses = []


class Course:
    """
    Represents a course in the school management system.

    Attributes:
        course_name (str): The name of the course.
        course_id (str): The unique identifier for the course.
        assigned_instructor (Instructor): The instructor assigned to the course.
        enrolled_students (list): A list of students enrolled in the course.
    """

    def __init__(self, course_name, course_id):
        """
        Initializes a new Course instance.

        Args:
            course_name (str): The name of the course.
            course_id (str): The unique identifier for the course.
        """
        self.course_name = course_name
        self.course_id = course_id
        self.assigned_instructor = None
        self.enrolled_students = []


class SchoolManagementSystem(QtWidgets.QWidget):
    """
    A GUI application for managing a school system, including students, instructors, and courses.

    Attributes:
        students (list): A list to store student information.
        instructors (list): A list to store instructor information.
        courses (list): A list to store course information.
    """

    def __init__(self):
        """
        Initializes the School Management System GUI.

        Sets the window title and geometry, initializes empty lists for students,
        instructors, and courses, and sets up the user interface.
        """
        super().__init__()
        self.setWindowTitle("School Management System")
        self.setGeometry(100, 100, 800, 600)

        self.students = []
        self.instructors = []
        self.courses = []

        self.init_ui()

    def clear_student_inputs(self):
        """Clears the input fields for student information."""
        self.student_name_input.clear()
        self.student_id_input.clear()
        self.student_email_input.clear()

    def clear_instructor_inputs(self):
        """Clears the input fields for instructor information."""
        self.instructor_name_input.clear()
        self.instructor_id_input.clear()
        self.instructor_email_input.clear()

    def clear_course_inputs(self):
        """Clears the input fields for course information."""
        self.course_name_input.clear()
        self.course_id_input.clear()

    def init_ui(self):
        """
        Initializes the user interface components and layout.

        Creates forms for adding students, instructors, and courses, as well as
        functionality for searching, registering students for courses, and assigning
        instructors to courses.
        """
        # Create a scroll area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # Create a widget to hold the main layout
        main_widget = QWidget()
        layout = QVBoxLayout()

        # Save and Load Buttons
        save_button = QPushButton("Save Data")
        save_button.clicked.connect(self.save_data)
        load_button = QPushButton("Load Data")
        load_button.clicked.connect(self.load_data)

        # Button to export to CSV
        self.export_csv_button = QPushButton("Export to CSV", self)
        self.export_csv_button.clicked.connect(self.export_to_csv)

        # Add Save/Load buttons to the layout
        layout.addWidget(save_button)
        layout.addWidget(load_button)
        layout.addWidget(self.export_csv_button)

        # Student Form
        student_group = QGroupBox("Add Student")
        student_layout = QVBoxLayout()
        self.student_name_input = QLineEdit()
        self.student_age_input = QLineEdit()
        self.student_email_input = QLineEdit()
        self.student_id_input = QLineEdit()
        student_layout.addWidget(QLabel("Name:"))
        student_layout.addWidget(self.student_name_input)
        student_layout.addWidget(QLabel("Age:"))
        student_layout.addWidget(self.student_age_input)
        student_layout.addWidget(QLabel("Email:"))
        student_layout.addWidget(self.student_email_input)
        student_layout.addWidget(QLabel("Student ID:"))
        student_layout.addWidget(self.student_id_input)
        self.add_student_button = QPushButton("Add Student")
        self.add_student_button.clicked.connect(self.add_student)
        student_layout.addWidget(self.add_student_button)
        student_group.setLayout(student_layout)
        layout.addWidget(student_group)

        # Instructor Form
        instructor_group = QGroupBox("Add Instructor")
        instructor_layout = QVBoxLayout()
        self.instructor_name_input = QLineEdit()
        self.instructor_email_input = QLineEdit()
        self.instructor_id_input = QLineEdit()
        instructor_layout.addWidget(QLabel("Name:"))
        instructor_layout.addWidget(self.instructor_name_input)
        instructor_layout.addWidget(QLabel("Email:"))
        instructor_layout.addWidget(self.instructor_email_input)
        instructor_layout.addWidget(QLabel("Instructor ID:"))
        instructor_layout.addWidget(self.instructor_id_input)
        self.add_instructor_button = QPushButton("Add Instructor")
        self.add_instructor_button.clicked.connect(self.add_instructor)
        instructor_layout.addWidget(self.add_instructor_button)
        instructor_group.setLayout(instructor_layout)
        layout.addWidget(instructor_group)

        # Course Form
        course_group = QGroupBox("Add Course")
        course_layout = QVBoxLayout()
        self.course_name_input = QLineEdit()
        self.course_id_input = QLineEdit()
        course_layout.addWidget(QLabel("Course Name:"))
        course_layout.addWidget(self.course_name_input)
        course_layout.addWidget(QLabel("Course ID:"))
        course_layout.addWidget(self.course_id_input)
        self.add_course_button = QPushButton("Add Course")
        self.add_course_button.clicked.connect(self.add_course)
        course_layout.addWidget(self.add_course_button)
        course_group.setLayout(course_layout)
        layout.addWidget(course_group)

        # Registration Form
        registration_group = QGroupBox("Register Student for Course")
        registration_layout = QVBoxLayout()
        self.student_combo = QComboBox()
        self.course_combo_reg = QComboBox()  # Separate dropdown for course selection in registration
        self.register_button = QPushButton("Register")
        self.register_button.clicked.connect(self.register_student_for_course)
        registration_layout.addWidget(QLabel("Select Student:"))
        registration_layout.addWidget(self.student_combo)
        registration_layout.addWidget(QLabel("Select Course:"))
        registration_layout.addWidget(self.course_combo_reg)  # Use the new course combo box
        registration_layout.addWidget(self.register_button)
        registration_group.setLayout(registration_layout)
        layout.addWidget(registration_group)

        # Assignment Form
        assignment_group = QGroupBox("Assign Instructor to Course")
        assignment_layout = QVBoxLayout()
        self.instructor_combo = QComboBox()
        self.course_combo_assign = QComboBox()  # Separate dropdown for course selection in assignment
        self.assign_button = QPushButton("Assign Instructor")
        self.assign_button.clicked.connect(self.assign_instructor_to_course)
        assignment_layout.addWidget(QLabel("Select Instructor:"))
        assignment_layout.addWidget(self.instructor_combo)
        assignment_layout.addWidget(QLabel("Select Course:"))
        assignment_layout.addWidget(self.course_combo_assign)  # Use the new course combo box
        assignment_layout.addWidget(self.assign_button)
        assignment_group.setLayout(assignment_layout)
        layout.addWidget(assignment_group)

        # Search Functionality
        search_group = QGroupBox("Search Records")
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_records)
        search_layout.addWidget(QLabel("Search:"))
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_button)
        search_group.setLayout(search_layout)
        layout.addWidget(search_group)

        # Table for Displaying Records
        self.table = QTableWidget()
        self.table.setColumnCount(4)  # Updated to 4 columns
        self.table.setHorizontalHeaderLabels(["Name", "ID", "Type", "Details"])
        self.table.setColumnWidth(3, 700)
        self.table.cellClicked.connect(self.populate_edit_fields)  # Populate fields when a cell is clicked
        layout.addWidget(self.table)

        # Edit and Delete Buttons
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit_record)
        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete_record)

        layout.addWidget(edit_button)
        layout.addWidget(delete_button)

        # Set the layout for the main widget and add it to the scroll area
        main_widget.setLayout(layout)
        scroll_area.setWidget(main_widget)

        # Set the main layout for the window
        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

        # Populate dropdowns initially
        self.update_dropdowns()

    def clear_dropdowns(self):
        """
        Clears all items from the dropdowns for students, instructors, and courses.
        """
        self.student_combo.clear()
        self.instructor_combo.clear()
        self.course_combo_reg.clear()
        self.course_combo_assign.clear()

    def update_dropdowns(self):
        """
        Updates the dropdown lists for students, instructors, and courses.

        Clears the existing dropdowns and populates them with the current 
        students, instructors, and courses from the respective lists.
        """
        self.clear_dropdowns()
        # Add students to dropdown
        for student in self.students:
            self.student_combo.addItem(student.name)
        # Add instructors to dropdown
        for instructor in self.instructors:
            self.instructor_combo.addItem(instructor.name)
        # Add courses to dropdown
        for course in self.courses:
            self.course_combo_reg.addItem(course.course_name)
            self.course_combo_assign.addItem(course.course_name)

    def is_valid_email(self, email):
        """
        Validates the given email address.

        Args:
        email (str): The email address to validate.

        Returns:
        bool: True if the email is valid, False otherwise.
        """
        # Basic regex for email validation
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    def populate_edit_fields(self, row, column):
        """
        Populates the input fields with the selected record's data from the table.

        Args:
        row (int): The row index of the selected table item.
        column (int): The column index of the selected table item.
        """
        if self.table.item(row, 2).text() == 'Student':
            # Populate student fields
            self.student_name_input.setText(self.table.item(row, 0).text())
            self.student_id_input.setText(self.table.item(row, 1).text())
            self.student_email_input.setText('')  # You may want to store and display email too
        elif self.table.item(row, 2).text() == 'Instructor':
        # Populate instructor fields
            self.instructor_name_input.setText(self.table.item(row, 0).text())
            self.instructor_id_input.setText(self.table.item(row, 1).text())
            self.instructor_email_input.setText('')  # You may want to store and display email too
        elif self.table.item(row, 2).text() == 'Course':
            # Populate course fields
            self.course_name_input.setText(self.table.item(row, 0).text())
            self.course_id_input.setText(self.table.item(row, 1).text())

    def add_student(self):
        """
        Adds a new student to the database and updates the student list.

        Retrieves the name from the input field, stores it in the database,
        and refreshes the displayed student list.
        """
        name = self.student_name_input.text()
        if name:
            connection = sqlite3.connect('school_management_system.db')
            cursor = connection.cursor()
            cursor.execute('INSERT INTO students (name) VALUES (?)', (name,))
            connection.commit()
            connection.close()
            self.load_students()
            self.name_input.clear()

    def load_students(self):
        """
        Loads the list of students from the database and displays them in the table.

        Fetches all students from the database and populates the table with their data.
        """
        connection = sqlite3.connect('school_management_system.db')
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM students')
        students = cursor.fetchall()
        connection.close()

        self.table.setRowCount(0)  # Clear the table
        for row_number, row_data in enumerate(students):
            self.table.insertRow(row_number)
        for column_number, data in enumerate(row_data):
            self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def add_instructor(self):
        """
        Adds a new instructor to the system and updates the instructor list.

        Retrieves the instructor details from input fields, creates a new 
        Instructor object, updates the list and dropdowns, and shows a success message.
        """
        name = self.instructor_name_input.text()
        instructor_id = self.instructor_id_input.text()
        email = self.instructor_email_input.text()  # New input
        if name and instructor_id:
            new_instructor = Instructor(name, email, instructor_id)
            self.instructors.append(new_instructor)
            self.update_table()
            self.update_dropdowns()  # Update dropdowns after adding
            QMessageBox.information(self, "Success", "Instructor added successfully.")
            self.clear_instructor_inputs()

    def add_course(self):
        """
        Adds a new course to the system and updates the course list.

        Retrieves the course details from input fields, creates a new 
        Course object, updates the list and dropdowns, and shows a success message.
        """
        course_name = self.course_name_input.text()
        course_id = self.course_id_input.text()
        if course_name and course_id:
            new_course = Course(course_name, course_id)
            self.courses.append(new_course)
            self.update_table()
            self.update_dropdowns()  # Update dropdowns after adding
            QMessageBox.information(self, "Success", "Course added successfully.")
            self.clear_course_inputs()

    def register_student_for_course(self):
        """
        Registers a student for a selected course.

        Retrieves the selected student and course from the dropdowns,
        updates the respective student and course objects, and refreshes the table.
        """
        selected_student = self.student_combo.currentText()
        selected_course = self.course_combo_reg.currentText()
        # Logic for registration
        if selected_student and selected_course:
            student = next((s for s in self.students if s.name == selected_student), None)
            course = next((c for c in self.courses if c.course_name == selected_course), None)
        if student and course:
            student.registered_courses.append(course.course_name)
            course.enrolled_students.append(student)
            self.update_table()

    def assign_instructor_to_course(self):
        """
        Assigns an instructor to a selected course.

        Retrieves the selected instructor and course from the dropdowns,
        updates the respective instructor and course objects, and refreshes the table.
        """
        selected_instructor = self.instructor_combo.currentText()
        selected_course = self.course_combo_assign.currentText()
        # Logic for assignment
        if selected_instructor and      selected_course:
            instructor = next((i for i in self.instructors if i.name == selected_instructor), None)
            course = next((c for c in self.courses if c.course_name == selected_course), None)
        if instructor and course:
            course.assigned_instructor = instructor
            instructor.assigned_courses.append(course.course_name)
            self.update_table()

    def edit_record(self):
        """
        Edits the selected record in the table.

        Retrieves the currently selected row, determines the type of record (Student, Instructor, or Course),
        and updates the corresponding fields based on the input values. If the record is found, it updates the
        record and refreshes the table and dropdowns.

        Displays a warning message if no record is selected or if the record is not found.
        """
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Error", "No record selected.")
            return

        record_type = self.table.item(selected_row, 2).text()

        if record_type == 'Student':
            name = self.student_name_input.text()
            student_id = self.student_id_input.text()
            email = self.student_email_input.text()

        if name and student_id:
            student = next((s for s in self.students if s.student_id == student_id), None)
            if student:
                student.name = name
                student.email = email  # Update email
                self.update_table()
                self.update_dropdowns()
                self.clear_student_inputs()
            else:
                QMessageBox.warning(self, "Error", "Student not found.")
        elif record_type == 'Instructor':
            name = self.instructor_name_input.text()
            instructor_id = self.instructor_id_input.text()
            email = self.instructor_email_input.text()

        if name and instructor_id:
            instructor = next((i for i in self.instructors if i.instructor_id == instructor_id), None)
            if instructor:
                instructor.name = name
                instructor.email = email  # Update email
                self.update_table()
                self.update_dropdowns()
                self.clear_instructor_inputs()
            else:
                QMessageBox.warning(self, "Error", "Instructor not found.")
        elif record_type == 'Course':
            course_name = self.course_name_input.text()
            course_id = self.course_id_input.text()

        if course_name and course_id:
            course = next((c for c in self.courses if c.course_id == course_id), None)
            if course:
                course.course_name = course_name
                self.update_table()
                self.update_dropdowns()
                self.clear_course_inputs()
            else:
                QMessageBox.warning(self, "Error", "Course not found.")

    def delete_record(self):
        """
        Deletes the selected record from the table.

        Retrieves the currently selected row and determines the type of record (Student, Instructor, or Course).
        Removes the record from the corresponding list and updates the table and dropdowns.

        Displays a warning message if no record is selected.
        """
        selected_row = self.table.currentRow()
        if selected_row < 0:
            QMessageBox.warning(self, "Error", "No record selected.")
        return

        record_type = self.table.item(selected_row, 2).text()

        if record_type == 'Student':
            student_id = self.table.item(selected_row, 1).text()
            self.students = [s for s in self.students if s.student_id != student_id]
        elif record_type == 'Instructor':
            instructor_id = self.table.item(selected_row, 1).text()
            self.instructors = [i for i in self.instructors if i.instructor_id != instructor_id]
        elif record_type == 'Course':
            course_id = self.table.item(selected_row, 1).text()
            self.courses = [c for c in self.courses if c.course_id != course_id]

        self.update_table()
        self.update_dropdowns()  # Update dropdowns after deleting

    def update_table(self):
        """
        Updates the table to display the current list of students, instructors, and courses.

        Clears the table and populates it with the latest data from the students, instructors, and courses lists.
        Each row displays the name, ID, type of record, and associated information such as registered courses or assigned instructors.

        Additionally, it updates the display for each record's enrolled students.
        """
        self.table.setRowCount(0)
        for student in self.students:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(student.name))
            self.table.setItem(row_position, 1, QTableWidgetItem(student.student_id))
            self.table.setItem(row_position, 2, QTableWidgetItem('Student'))
            self.table.setItem(row_position, 3, QTableWidgetItem(', '.join(student.registered_courses)))

        for instructor in self.instructors:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(instructor.name))
            self.table.setItem(row_position, 1, QTableWidgetItem(instructor.instructor_id))
            self.table.setItem(row_position, 2, QTableWidgetItem('Instructor'))
            self.table.setItem(row_position, 3, QTableWidgetItem(', '.join(instructor.assigned_courses)))

        for course in self.courses:
            row_position = self.table.rowCount()
            self.table.insertRow(row_position)
            self.table.setItem(row_position, 0, QTableWidgetItem(course.course_name))
            self.table.setItem(row_position, 1, QTableWidgetItem(course.course_id))
            self.table.setItem(row_position, 2, QTableWidgetItem('Course'))
            self.table.setItem(row_position, 3, QTableWidgetItem(f"Instructor: {course.assigned_instructor.name if course.assigned_instructor else 'None'}, "f"Enrolled Students: {', '.join(s.name for s in course.enrolled_students) if course.enrolled_students else 'None'}"))
    
    def search_records(self):
        """
        Searches for records in the table based on the input text.

        Retrieves the search text from the input field and iterates through each row of the table.
        Rows containing the search text in the first column (name) are made visible, while others are hidden.

        The search is case-insensitive.
        """
        search_text = self.search_input.text().lower()
        for i in range(self.table.rowCount()):
            item = self.table.item(i, 0)
            if item and search_text in item.text().lower():
                self.table.setRowHidden(i, False)
            else:
                self.table.setRowHidden(i, True)

    def save_data(self):
        """
        Saves the current data of students, instructors, and courses to a file.

        The data is serialized using the pickle module and written to a file named "school_data.pkl".
        Displays a success message upon successful saving or an error message if an exception occurs.

        Returns:
            None
        """
        data = {
            "students": self.students,
            "instructors": self.instructors,
            "courses": self.courses
        }
        try:
            with open("school_data.pkl", "wb") as file:
                pickle.dump(data, file)
                QMessageBox.information(self, "Success", "Data saved successfully.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to save data: {str(e)}")

    def load_data(self):
        """
        Loads data from a file into the application.

        Attempts to read the data from "school_data.pkl" using the pickle module. 
        If successful, updates the lists of students, instructors, and courses, 
        and refreshes the table and dropdowns with the loaded data. 
        Displays success or error messages based on the outcome.

        Returns:
            None
        """
        try:
            with open("school_data.pkl", "rb") as file:
                data = pickle.load(file)
                self.students = data.get("students", [])
                self.instructors = data.get("instructors", [])
                self.courses = data.get("courses", [])
        
                self.update_table()  # Refresh the table with loaded data
                self.update_dropdowns()  # Refresh the dropdowns with loaded data
                QMessageBox.information(self, "Success", "Data loaded successfully.")
        except FileNotFoundError:
            QMessageBox.warning(self, "Error", "No saved data file found.")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to load data: {str(e)}")

    def export_to_csv(self):
        """
        Exports the data of instructors to a CSV file.

        Opens a file dialog for the user to choose a location and name for the CSV file.
        Writes the data of instructors, including name, ID, type, and assigned courses, into the file.
        Displays a success message after the export.

        Returns:
            None
        """
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getSaveFileName(self, "Save CSV File", "", "CSV Files (*.csv);;All Files (*)", options=options)
    
        if file_name:
            with open(file_name, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "ID", "Type", "Details"])  # Write header
            
            for instructor in self.instructors:
                writer.writerow([instructor.name, instructor.instructor_id, 'Instructor', ', '.join(instructor.assigned_courses)])
        
        QMessageBox.information(self, "Success", "Data exported successfully to CSV.")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = SchoolManagementSystem()
    window.show()
    sys.exit(app.exec_())


            

