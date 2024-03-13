import math

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
        total_credits = sum(course_credits.get(course_id, 0) for course_id in self.marks)
        if total_credits == 0:
            return 0
        weighted_sum = sum(self.marks.get(course_id, 0) * course_credits.get(course_id, 0) for course_id in self.marks)
        return weighted_sum / total_credits

class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.id = course_id
    