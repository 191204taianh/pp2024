import math
import numpy as np
import curses

class Student:
    def __init__(self, name, student_id, dob):
        self.name = name
        self.id = student_id
        self.dob = dob
        self.marks = {}

    def input_marks(self, course):
        marks = float(input(f"Input mark for {course.name} for student {self.name}: "))
        marks = math.floor(marks * 10) / 10  # Round down to 1 decimal place
        self.marks[course.id] = marks

    def calculate_average_gpa(self, course_credits):
        total_credits = 0
        weighted_sum = 0
        for course_id, marks in self.marks.items():
            total_credits += course_credits.get(course_id, 0)
            weighted_sum += course_credits.get(course_id, 0) * marks
        if total_credits == 0:
            return 0
        return weighted_sum / total_credits

class Course:
    def __init__(self, name, course_id, credits):
        self.name = name
        self.id = course_id
        self.credits = credits


class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_student_num(self):
        return int(input("Input the number of students: "))

    def input_course_num(self):
        return int(input("Input the number of courses: "))

    def input_student_info(self):
        return Student(
            input("Enter student name: "),
            input("Enter student ID: "),
            input("Enter student date of birth (DD-MM-YYYY): "),
        )

    def input_course_info(self):
        return Course(input("Enter course name: "), input("Enter course ID: "), float(input("Enter course credits: ")))

    def student_list(self, stdscr):
        stdscr.clear()
        stdscr.addstr("\n-----------------------\n")
        stdscr.addstr("Student(s) in the list:\n")
        stdscr.addstr("-----------------------\n")
        for student in self.students:
            stdscr.addstr(f"Student ID: {student.id : <10} | Student name: {student.name : <30} | Student DoB: {student.dob}\n")
        stdscr.refresh()

    def courses_list(self, stdscr):
        stdscr.addstr("\n---------------------\n")
        stdscr.addstr("Course(s) in the list:\n")
        stdscr.addstr("----------------------\n")
        for course in self.courses:
            stdscr.addstr(f"Course ID: {course.id: <10} | Course name: {course.name} | Course credits: {course.credits}\n")
        stdscr.refresh()

    def student_mark_course_info(self, student, course):
        print(f"\nStudent: {student.name} -> Course: {course.name}")
        marks = student.marks.get(course.id, "Marks not available")
        print(f"Marks: {marks}")

    def main(self, stdscr):
        curses.curs_set(0)
        stdscr.clear()
        student_count = self.input_student_num()
        for _ in range(student_count):
            student_info = self.input_student_info()
            self.students.append(student_info)

        course_count = self.input_course_num()
        for _ in range(course_count):
            course_info = self.input_course_info()
            self.courses.append(course_info)

        self.student_list(stdscr)
        self.courses_list(stdscr)

        for student in self.students:
            for course in self.courses:
                student.input_marks(course)

        course_credits = {course.id: course.credits for course in self.courses}

        gpa_list = []
        for student in self.students:
            avg_gpa = student.calculate_average_gpa(course_credits)
            gpa_list.append((student, avg_gpa))

        gpa_list.sort(key=lambda x: x[1], reverse=True)

        stdscr.addstr("\nStudent list sorted by GPA descending:\n")
        stdscr.addstr("------------------------------------------------------------\n")
        for student, gpa in gpa_list:
            stdscr.addstr(f"Student ID: {student.id : <10} | Student name: {student.name : <30} | GPA: {gpa:.2f}\n")
        stdscr.addstr("------------------------------------------------------------\n")
        stdscr.refresh()

        choose_student = input("\nChoose student to show marks (student ID): ")
        choose_course = input("Choose course to show marks (course ID): ")

        selected_student = next(
            (student for student in self.students if student.id == choose_student), None
        )
        selected_course = next(
            (course for course in self.courses if course.id == choose_course), None
        )

        if selected_student and selected_course:
            self.student_mark_course_info(selected_student, selected_course)
        else:
            print("No student or course found in the list !!!")


def main(stdscr):
    school_system = SchoolSystem()
    school_system.main(stdscr)
    stdscr.getch()

curses.wrapper(main)