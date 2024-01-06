def process_students(num_students):
    # Perform some operations based on the number of students
    if num_students < 0:
        print("Invalid number of students.")
    elif num_students == 0:
        print("There are no students.")
    else:
        print(f"There are {num_students} students.")

num_students = int(input("Enter the number of students: "))
process_students(num_students)