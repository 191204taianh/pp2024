import math

def input_student_num():
    num_students = int(input("Input the number of students: "))
    with open("students.txt", "w") as file:
        file.write(f"Number of students: {num_students}\n")
    return num_students

def input_course_num():
    num_courses = int(input("Input the number of courses: "))
    with open("courses.txt", "w") as file:
        file.write(f"Number of courses: {num_courses}\n")
    return num_courses

def input_student_info():
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    dob = input("Enter student date of birth (DD-MM-YYYY): ")
    with open("students.txt", "a") as file:
        file.write(f"Student name: {name}, Student ID: {student_id}, DoB: {dob}\n")
    return name, student_id, dob

def input_course_info():
    name = input("Enter course name: ")
    course_id = input("Enter course ID: ")
    with open("courses.txt", "a") as file:
        file.write(f"Course name: {name}, Course ID: {course_id}\n")
    return name, course_id

def input_marks(student, course):
    marks = float(input(f"Input mark for {course.name} for student {student.name}: "))
    marks = math.floor(marks * 10) / 10  # Round down to 1 decimal place
    student.marks[course.id] = marks
    with open("marks.txt", "a") as file:
        file.write(f"Student: {student.name}, Course: {course.name}, Marks: {marks}\n")
