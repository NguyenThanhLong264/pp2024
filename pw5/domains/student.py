import math
import numpy as np
from domains.course import Course

class Student:
    def __init__(self,student_id, name, dob):
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
            course = Course.find_course_by_id(course_id)
            if course:
                credits.append(course.credits)  # Assuming you have a 'credits' attribute in the Course class
                marks.append(mark)

        if len(credits) == 0:
            return 0.0

        weighted_sum = np.dot(credits, marks)
        total_credits = np.sum(credits)
        average_gpa = weighted_sum / total_credits

        return average_gpa