import os
import gzip
import pickle
import tkinter as tk
from tkinter import messagebox
from domains import Student, Course
from input import input_student_num, input_student_info, input_course_num, input_course_info, input_marks
from output import print_student_mark_course_info

class SchoolSystemGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("School System")
        
        self.students = []
        self.courses = []

        self.load_data()

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)

        self.student_button = tk.Button(self.main_frame, text="Input Students", command=self.input_students)
        self.student_button.grid(row=0, column=0, padx=10, pady=5)

        self.course_button = tk.Button(self.main_frame, text="Input Courses", command=self.input_courses)
        self.course_button.grid(row=0, column=1, padx=10, pady=5)

        self.calculate_button = tk.Button(self.main_frame, text="Calculate GPA", command=self.calculate_gpa)
        self.calculate_button.grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    def input_students(self):
        num_students = input_student_num()
        for _ in range(num_students):
            student_info = input_student_info()
            self.students.append(Student(*student_info))

    def input_courses(self):
        num_courses = input_course_num()
        for _ in range(num_courses):
            course_info = input_course_info()
            self.courses.append(Course(*course_info))

    def calculate_gpa(self):
        for student in self.students:
            for course in self.courses:
                input_marks(student, course)

        course_credits = {}
        for course in self.courses:
            credit = float(input(f"Enter credits for course {course.name}: "))
            course_credits[course.id] = credit

        for student in self.students:
            gpa = student.calculate_average_gpa(course_credits)
            messagebox.showinfo("GPA", f"Average GPA for student {student.name}: {gpa:.2f}")

    def load_data(self):
        if os.path.exists('data.pkl.gz'):
            with gzip.open('data.pkl.gz', 'rb') as f:
                self.students, self.courses = pickle.load(f)

    def save_data(self):
        with gzip.open('data.pkl.gz', 'wb') as f:
            pickle.dump((self.students, self.courses), f)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.save_data()
            self.root.destroy()

def main():
    root = tk.Tk()
    app = SchoolSystemGUI(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()

if __name__ == "__main__":
    main()
