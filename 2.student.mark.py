class Student:
    def __init__(self, name, student_id, dob):
        self.name = name
        self.id = student_id
        self.dob = dob
        self.marks = {}

    def input_marks(self, course):
        marks = float(input(f"Input mark for {course.name} for student {self.name}: "))
        self.marks[course.id] = marks


class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.id = course_id


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
        return Course(input("Enter course name: "), input("Enter course ID: "))

    def student_list(self):
        print("\n-----------------------")
        print("Student(s) in the list:")
        print("-----------------------")
        for student in self.students:
            print(f"Student ID: {student.id : <10} | Student name: {student.name : <30} | Student DoB: {student.dob}")

    def courses_list(self):
        print("\n---------------------")
        print("Course(s) in the list:")
        print("----------------------")
        for course in self.courses:
            print(f"Course ID: {course.id: <10} | Course name: {course.name}")

    def student_mark_course_info(self, student, course):
        print(f"\nStudent: {student.name} -> Course: {course.name}")
        marks = student.marks.get(course.id, "Marks not available")
        print(f"Marks: {marks}")

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

        # Example of using listing functions
        self.student_list()
        self.courses_list()

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


# Instantiate the SchoolSystem class and run the program
school_system = SchoolSystem()
school_system.main()
    