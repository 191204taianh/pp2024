import os
import gzip
import pickle
import shutil
from domains import Student, Course
from input import input_student_num, input_student_info, input_course_num, input_course_info, input_marks
from output import print_student_mark_course_info

def compress_files():
    with gzip.open('students.pkl.gz', 'wb') as f_out:
        for filename in ['domains.py', 'input.py', 'output.py', 'main.py']:
            with open(filename, 'rb') as f_in:
                shutil.copyfileobj(f_in, f_out)

def decompress_files():
    if os.path.exists('students.pkl.gz'):
        with gzip.open('students.pkl.gz', 'rb') as f_in:
            for filename in ['domains.py', 'input.py', 'output.py', 'main.py']:
                with open(filename, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)

def save_data(students, courses):
    with open('data.pkl', 'wb') as f:
        pickle.dump((students, courses), f)

def load_data():
    if os.path.exists('data.pkl'):
        with open('data.pkl', 'rb') as f:
            return pickle.load(f)
    else:
        return [], []

def main():
    # Decompress files if students.pkl.gz exists
    decompress_files()

    class SchoolSystem:
        def __init__(self, students=None, courses=None):
            self.students = students if students else []
            self.courses = courses if courses else []

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
                    input_marks(student, course)

            # Calculate GPA for each student and print
            course_credits = {course.id: float(input(f"Enter credits for course {course.name}: ")) for course in self.courses}
            for student in self.students:
                gpa = student.calculate_average_gpa(course_credits)
                print(f"Average GPA for student {student.name}: {gpa:.2f}")

            # Sorting and other functionalities remain the same
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

    # Instantiate the SchoolSystem class and run the program
    students, courses = load_data()
    school_system = SchoolSystem(students, courses)
    school_system.main()

    # At the end of your program, after closing:
    # Save data and compress all files into students.pkl.gz
    save_data(school_system.students, school_system.courses)
    compress_files()

if __name__ == "__main__":
    main()
