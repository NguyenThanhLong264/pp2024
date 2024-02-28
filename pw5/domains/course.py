import curses


class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    @staticmethod
    def find_course_by_id(course_id):
        # Assuming you have a global list of courses
        for course in curses:
            if course.course_id == course_id:
                return course
        return None