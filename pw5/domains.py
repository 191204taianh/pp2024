import os

class SchoolSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_student_num(self):
        return int(input("Input the number of students: "))

    def input_course_num(self):
        return int(input("Input the number of courses: "))

    def input_student_info(self):
        student = Student(
            input("Enter student name: "),
            input("Enter student ID: "),
            input("Enter student date of birth (DD-MM-YYYY): "),
        )
        self.students.append(student)

        with open("students.txt", "a") as file:
            file.write(f"{student.name},{student.id},{student.dob}\n")

        return student

    def input_course_info(self):
        course = Course(input("Enter course name: "), input("Enter course ID: "))
        self.courses.append(course)

        with open("courses.txt", "a") as file:
            file.write(f"{course.name},{course.id}\n")

        return course

    def input_marks(self, course):
        student_id = input("Enter student ID: ")
        student = next((student for student in self.students if student.id == student_id), None)
        if student:
            marks = float(input(f"Input mark for {course.name} for student {student.name}: "))
            marks = math.floor(marks * 10) / 10  # Round down to 1 decimal place
            student.marks[course.id] = marks

            with open("marks.txt", "a") as file:
                file.write(f"{student.id},{course.id},{marks}\n")
        else:
            print("Student not found!")

    def main(self):
        student_count = self.input_student_num()
        for _ in range(student_count):
            student_info = self.input_student_info()
            self.students.append(student_info)

        course_count = self.input_course_num()
        for _ in range(course_count):
            course_info = self.input_course_info()
            self.courses.append(course_info)

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
            self.student_mark_course_info(selected_student, selected_course)
        else:
            print("No student or course found in the list !!!")
