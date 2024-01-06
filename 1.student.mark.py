students = []
courses = []

# Input functions

def input_studentNum():
    return int(input("Input the number of students: "))

def input_courseNum():
    return int(input("Input the number of courses: "))

def input_studentInfo():
    return {'name': input("Enter student name: "),
            'id': input("Enter student ID: "),
            'dob': input("Enter student date of birth (DD-MM-YYYY): "),
            'marks': {}}

def input_courseInfo():
    return {'name': input("Enter course name: "),
            'id': input("Enter course ID: ")}

def input_studentMark(course):
    marks = float(input(f"Input mark for {course['name']} for student {student['name']}: "))
    return marks

# Listing functions

def student_list():
    print("\n-----------------------")
    print("Student(s) in the list:")
    print("-----------------------")
    for student in students:
        print(f"Student ID: {student['id'] : <10} | Student name: {student['name'] : <30} | Student DoB: {student['dob']}")

def courses_list():
    print("\n---------------------")
    print("Course(s) in the list:")
    print("----------------------")
    for course in courses:
        print(f"Course ID: {course['id']: <10} | Course name: {course['name']}")

# Function to print marks

def studentMark_courseInfo(student, course):
    print(f"\nStudent: {student['name']} -> Course: {course['name']}")
    marks = student['marks'].get(course['id'], "Marks not available")
    print(f"Marks: {marks}")

# Main
    
student = input_studentNum()

for _ in range(student):
    student_info = input_studentInfo()
    students.append(student_info)

course = input_courseNum()

for _ in range(course):
    course_info = input_courseInfo()
    courses.append(course_info)

for student in students:
    for course in courses:
        student['marks'][course['id']] = input_studentMark(course)

# Example of using listing functions 
student_list()
courses_list()

choose_student = input("\nChoose student to show marks (student ID): ")
choose_course = input("Choose course to show marks (course ID): ")

selected_student = next((student for student in students if student['id'] == choose_student), None)
selected_course = next((course for course in courses if course['id'] == choose_course), None)

if selected_student and selected_course:
    studentMark_courseInfo(selected_student, selected_course)
else:
    print("No student or course found in the list !!!")
