import os
import math
from domains import Student, Course
from input import input_student_num, input_student_info, input_course_num, input_course_info
from output import print_student_list, print_courses_list, print_student_mark_course_info

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def main(self):
        student_count = input_student_num()
        for _ in range(student_count):
            name, student_id, dob = input_student_info()
            student = Student(name, student_id, dob)
            self.students.append(student)

        course_count = input_course_num()
        for _ in range(course_count):
            name, course_id = input_course_info()
            course = Course(name, course_id)
            self.courses.append(course)

        for student in self.students:
            for course in self.courses:
                student.input_marks(course)

        # Calculate GPA for each student
        course_credits = {course.id: float(input(f"Enter credits for course {course.name}: ")) for course in self.courses}
        for student in self.students:
            gpa = student.calculate_average_gpa(course_credits)
            print(f"Average GPA for student {student.name}: {gpa:.2f}")

        # Sort students by GPA descending
        self.students.sort(key=lambda student: student.calculate_average_gpa(course_credits), reverse=True)
        print("\nStudents sorted by GPA descending:")
        for student in self.students:
            print(f"Student ID: {student.id}, Name: {student.name}, GPA: {student.calculate_average_gpa(course_credits):.2f}")

        choose_student = input("\nChoose student to show marks (student ID): ")
        choose_course = input("Choose course to show marks (course ID): ")

        selected_student = next(
            (student for student in self.students if student.id == choose_student), None
        )
        selected_course = next(
            (course for course in self.courses if course.id == choose_course), None
        )

        if selected_student and selected_course:
            print_student_mark_course_info(selected_student, selected_course)
        else:
            print("No student or course found in the list !!!")

if __name__ == "__main__":
    school_system = SchoolSystem()
    school_system.main()
