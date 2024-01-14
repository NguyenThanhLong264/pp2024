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


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name


class StudentManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")

        student = Student(student_id, name, dob)
        self.students.append(student)

    def input_courses(self):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")

        course = Course(course_id, name)
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
        student.add_marks(course_id, marks_for_course)

    def list_courses(self):
        if len(self.courses) == 0:
            print("No courses available.")
            return

        print("ID\tName")
        for course in self.courses:
            print(f"{course.course_id}\t{course.name}")

    def list_students(self):
        if len(self.students) == 0:
            print("No students available.")
            return

        print("ID\tName\tDoB")
        for student in self.students:
            print(f"{student.student_id}\t{student.name}\t{student.dob}")

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

    def menu(self):
        while True:
            print("\n===== MENU =====")
            print("1. Input data for students")
            print("2. Input courses")
            print("3. List students")
            print("4. List courses")
            print("5. Choose course for students")
            print("6. Show students mark")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.input_students()
            elif choice == '2':
                self.input_courses()
            elif choice == '3':
                self.list_students()
            elif choice == '4':
                self.list_courses()
            elif choice == '5':
                self.select_course()
            elif choice == '6':
                self.show_student_marks()
            elif choice == '0':
                print("Closing program.....")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    system = StudentManagementSystem()
    system.menu()