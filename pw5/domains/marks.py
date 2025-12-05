import math

class Marks:
    def __init__(self):
        self.tab_marks = {}

    def create_tab(self, tab_students, tab_courses):
        for cid, course in tab_courses.items():
            for sid, student in tab_students.items():
                while True:
                    raw = input(
                        f"Enter marks for {student.name} in {course.name} (separated by spaces): "
                    )
                    parts = raw.split()

                    try:
                        scores = [math.floor(float(x)*10)/10 for x in parts]
                        break
                    except ValueError:
                        print("Please enter only numeric marks.")

                student.marks[cid] = scores
                student.credits[cid] = course.credit
