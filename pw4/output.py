def print_student_list(students):
    print("\n-----------------------")
    print("Student(s) in the list:")
    print("-----------------------")
    for student in students:
        print(
            f"Student ID: {student.id : <10} | Student name: {student.name : <30} | Student DoB: {student.dob}"
        )

def print_courses_list(courses):
    print("\n---------------------")
    print("Course(s) in the list:")
    print("----------------------")
    for course in courses:
        print(f"Course ID: {course.id: <10} | Course name: {course.name}")

def print_student_mark_course_info(student, course):
    print(f"\nStudent: {student.name} -> Course: {course.name}")
    marks = student.marks.get(course.id, "Marks not available")
    print(f"Marks: {marks}")
