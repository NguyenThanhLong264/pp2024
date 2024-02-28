import math
from domains.student import Student
from domains.course import Course

def input_students():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")

    student = Student(student_id, name, dob)

    with open("students.txt", "a") as f:
        f.write(f"{student_id},{name},{dob}\n")

    return student

def input_courses():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")
    credits = int(input("Enter course credits: "))

    course = Course(course_id, name, credits)

    with open("courses.txt", "a") as f:
        f.write(f"{course_id},{name},{credits}\n")

    return course

def select_course(students, courses):
    print("Available courses:")
    list_courses(courses)
    course_id = input("Enter the course ID: ")

    course = find_course_by_id(courses, course_id)
    if not course:
        print("Invalid course ID. Please try again.")
        return

    print("Available students:")
    list_students(students)
    student_id = input("Enter the student ID: ")

    student = find_student_by_id(students, student_id)
    if not student:
        print("Invalid student ID. Please try again.")
        return

    marks_for_course = float(input(f"Enter marks for student {student.name} in course {course.name}: "))
    rounded_marks = math.floor(marks_for_course * 10) / 10
    student.add_marks(course_id, rounded_marks)

    with open("marks.txt", "a") as f:
        f.write(f"{student_id},{course_id},{rounded_marks}\n")

def list_courses(courses):
    if len(courses) == 0:
        print("No courses available.")
        return

    print("ID\tName\tCredits")
    for course in courses:
        print(f"{course.course_id}\t{course.name}\t{course.credits}")

def list_students(students):
    if len(students) == 0:
        print("No students available.")
        return

    sorted_students = sorted(students, key=lambda student: student.calculate_average_gpa(), reverse=True)

    print("ID\tName\tDoB\tGPA")
    for student in sorted_students:
        gpa = student.calculate_average_gpa()
        print(f"{student.student_id}\t{student.name}\t{student.dob}\t{gpa:.1f}")

def find_student_by_id(students, student_id):
    for student in students:
        if student.student_id == student_id:
            return student
    return None

def find_course_by_id(courses, course_id):
    for course in courses:
        if course.course_id == course_id:
            return course
    return None

def show_student_marks(students, courses):
    print("Available courses:")
    list_courses(courses)
    course_id = input("Enter the course ID: ")

    for student in students:
        marks = student.get_marks(course_id)
        if marks:
            print(f"Student {student.name} marks in course {find_course_by_id(courses, course_id).name}: {marks}")
        else:
            print(f"No marks found for student {student.name} in course {find_course_by_id(courses, course_id).name}")