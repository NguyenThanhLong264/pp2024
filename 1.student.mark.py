students = []
courses = []
marks = {}

def input_students():
    num_students = int(input("Enter the number of students: "))

    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")

        student = (student_id, name, dob)
        students.append(student)


def input_courses():
    num_courses = int(input("Enter the number of courses: "))

    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")

        course = (course_id, name)
        courses.append(course)


def select_course():
    print("Available courses:")
    list_courses()
    course_id = input("Enter the course ID: ")

    for student in students:
        student_id = student[0]
        marks[student_id] = {}

        marks_for_course = float(input(f"Enter marks for student {student[1]} in course {course_id}: "))
        marks[student_id][course_id] = marks_for_course


def list_courses():
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")


def list_students():
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")


def show_student_marks():
    print("Available courses:")
    list_courses()
    course_id = input("Enter the course ID: ")

    for student in students:
        student_id = student[0]

        if course_id in marks.get(student_id, {}):
            print(f"Student {student[1]} marks in course {course_id}: {marks[student_id][course_id]}")
        else:
            print(f"No marks found for student {student[1]} in course {course_id}")


def main():
    input_students()
    input_courses()

    while True:
        print("\n===== MENU =====")
        print("1. Select a course and input student marks")
        print("2. List courses")
        print("3. List students")
        print("4. Show student marks for a given course")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            select_course()
        elif choice == '2':
            list_courses()
        elif choice == '3':
            list_students()
        elif choice == '4':
            show_student_marks()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()