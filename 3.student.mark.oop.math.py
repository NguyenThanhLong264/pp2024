import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.marks = {}

    def add_marks(self, course_id, marks):
        self.marks[course_id] = marks

    def get_marks(self, course_id):
        return self.marks.get(course_id, None)

    def calculate_average_gpa(self):
        credits = []  # List of credits for each course
        marks = []  # List of marks for each course

        for course_id, mark in self.marks.items():
            course = self.find_course_by_id(course_id)
            if course:
                credits.append(course.credits)  # Assuming you have a 'credits' attribute in the Course class
                marks.append(mark)

        if len(credits) == 0:
            return 0.0

        weighted_sum = np.dot(credits, marks)
        total_credits = np.sum(credits)
        average_gpa = weighted_sum / total_credits

        return average_gpa


class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

        # Initialize curses
        self.stdscr = curses.initscr()
        curses.cbreak()
        curses.noecho()
        self.stdscr.keypad(True)

    def input_students(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")

        student = Student(student_id, name, dob)
        self.students.append(student)

    def input_courses(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credits = int(input("Enter course credits: "))

        course = Course(course_id, name, credits)
        self.courses.append(course)

    def select_course(self):
        print("Available courses:")
        self.list_courses()
        course_id = input("Enter the course ID: ")

        course = self.find_course_by_id(course_id)
        if not course:
            print("Invalid course ID. Please try again.")
            return

        print("Available students:")
        self.list_students()
        student_id = input("Enter the student ID: ")

        student = self.find_student_by_id(student_id)
        if not student:
            print("Invalid student ID. Please try again.")
            return

        marks_for_course = float(input(f"Enter marks for student {student.name} in course {course.name}: "))
        rounded_marks = math.floor(marks_for_course * 10) / 10
        student.add_marks(course_id, rounded_marks)

    def list_courses(self):
        if len(self.courses) == 0:
            print("No courses available.")
            return

        print("ID\tName\tCredits")
        for course in self.courses:
            print(f"{course.course_id}\t{course.name}\t{course.credits}")

    def list_students(self):
        if len(self.students) == 0:
            print("No students available.")
            return

        sorted_students = sorted(self.students, key=lambda student: student.calculate_average_gpa(), reverse=True)

        print("ID\tName\tDoB\tGPA")
        for student in sorted_students:
            gpa = student.calculate_average_gpa()
            print(f"{student.student_id}\t{student.name}\t{student.dob}\t{gpa:.1f}")

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def find_course_by_id(self, course_id):
        for course in self.courses:
            if course.course_id == course_id:
                return course
        return None

    def show_student_marks(self):
        print("Available courses:")
        self.list_courses()
        course_id = input("Enter the course ID: ")

        for student in self.students:
            marks = student.get_marks(course_id)
            if marks:
                print(f"Student {student.name} marks in course {self.find_course_by_id(course_id).name}: {marks}")
            else:
                print(f"No marks found for student {student.name} in course {self.find_course_by_id(course_id).name}")

    def main(self):
        while True:
            self.stdscr.clear()
            self.stdscr.addstr("\n===== MENU =====\n")
            self.stdscr.addstr("1. Input data for students\n")
            self.stdscr.addstr("2. Input courses\n")
            self.stdscr.addstr("3. List students\n")
            self.stdscr.addstr("4. List courses\n")
            self.stdscr.addstr("5. Choose course for students\n")
            self.stdscr.addstr("6. Show students mark\n")
            self.stdscr.addstr("0. Exit\n")

            self.stdscr.refresh()

            choice = self.stdscr.getch()

            if choice == ord('1'):
                self.input_students()
            elif choice == ord('2'):
                self.input_courses()
            elif choice == ord('3'):
                self.list_students()
            elif choice == ord('4'):
                self.list_courses()
            elif choice == ord('5'):
                self.select_course()
            elif choice == ord('6'):
                self.show_student_marks()
            elif choice == ord('0'):
                self.stdscr.addstr("Closing program.....")
                self.stdscr.refresh()
                break
            else:
                self.stdscr.addstr("Invalid choice. Please try again.")
                self.stdscr.refresh()

        # End curses
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()


if __name__ == "__main__":
    sms = StudentManagementSystem()
    sms.main()