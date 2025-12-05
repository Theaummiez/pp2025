import math

class Marks:
    def __init__(self):
        self.tab_marks = {}

    def create_tab(self, students, courses, input_func):
        """
        Get marks for every student and course.
        """
        for cid, course in courses.items():
            for sid, student in students.items():
                while True:
                    raw = input_func(
                        f"Enter marks for {student.name} in {course.name} (space separated): "
                    )
                    parts = raw.split()
                    try:
                        scores = [math.floor(float(x) * 10) / 10 for x in parts]
                        break
                    except ValueError:
                        print("Please enter numeric scores separated by space.")

                student.marks[cid] = scores
                student.credits[cid] = course.credit
