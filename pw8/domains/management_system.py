from domains.student import Student
from domains.course import Course
from output import initialize_curses, close_curses, display_menu, display_message
from input import input_students, input_courses, select_course, list_students, list_courses, show_student_marks, find_student_by_id, find_course_by_id

class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.stdscr = None

    def input_students(self):
        student = input_students()
        self.students.append(student)

    def input_courses(self):
        course = input_courses()
        self.courses.append(course)

    def select_course(self):
        select_course(self.students, self.courses)

    def list_courses(self):
        list_courses(self.courses)

    def list_students(self):
        list_students(self.students)

    def show_student_marks(self):
        show_student_marks(self.students, self.courses)

    def main(self):
        self.stdscr = initialize_curses()

        while True:
            display_menu(self.stdscr)

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
                display_message(self.stdscr, "Closing program.....")
                break
            else:
                display_message(self.stdscr, "Invalid choice. Please try again.")

        close_curses(self.stdscr)