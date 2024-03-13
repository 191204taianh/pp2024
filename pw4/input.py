def input_student_num():
    return int(input("Input the number of students: "))

def input_course_num():
    return int(input("Input the number of courses: "))

def input_student_info():
    return (
        input("Enter student name: "),
        input("Enter student ID: "),
        input("Enter student date of birth (DD-MM-YYYY): "),
    )

def input_course_info():
    return input("Enter course name: "), input("Enter course ID: ")
