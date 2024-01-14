students = []
courses = []
marks = {}

def input_students():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")

    student = (student_id, name, dob)
    students.append(student)


def input_courses():
    course_id = input("Enter course ID: ")
    name = input("Enter course name: ")

    course = (course_id, name)
    courses.append(course)


def select_course():
    print("Available courses:")
    list_courses()
    course_id = input("Enter the course ID: ")

    if course_id not in [course[0] for course in courses]:
        print("Invalid course ID. Please try again.")
        return

    print("Available students:")
    list_students()
    student_id = input("Enter the student ID: ")

    if student_id not in [student[0] for student in students]:
        print("Invalid student ID. Please try again.")
        return

    if course_id in marks.get(student_id, {}):
        print(f"Student {students[student_id][1]} is already enrolled in course {course_id}.")
    else:
        marks_for_course = float(input(f"Enter marks for student {students[student_id][1]} in course {course_id}: "))
        marks[student_id][course_id] = marks_for_course


def list_courses():
    if len(courses) == 0:
        print("No courses available.")
        return

    print("ID\tName")
    for course in courses:
        print(f"{course[0]}\t{course[1]}")


def list_students():
    if len(students) == 0:
        print("No students available.")
        return

    print("ID\tName\tDoB")
    for student in students:
        print(f"{student[0]}\t{student[1]}\t{student[2]}")


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
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            list_students()
        elif choice == '4':
            list_courses()
        elif choice == '5':
            select_course()
        elif choice == '6':
            show_student_marks()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()