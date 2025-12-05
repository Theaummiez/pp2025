import math
import numpy as np

def input_students(Student):
    n = int(input("How many students? "))
    students = Student.Create_tab(n)

    # write to file
    with open("students.txt", "w", encoding="utf-8") as f:
        for s in students.values():
            f.write(f"{s.id},{s.name},{s.dob}\n")

    return students


def input_courses(Courses):
    c = int(input("How many courses? "))
    courses = Courses.create_tab(c)

    # write to file
    with open("courses.txt", "w", encoding="utf-8") as f:
        for course in courses.values():
            f.write(f"{course.id},{course.name},{course.credit}\n")

    return courses


def input_marks(tab_students, tab_courses, Marks):
    marks = Marks()
    marks.create_tab(tab_students, tab_courses)

    # write marks to marks.txt
    with open("marks.txt", "w", encoding="utf-8") as f:
        for sid, student in tab_students.items():
            for cid, scores in student.marks.items():
                score_str = " ".join(map(str, scores))
                f.write(f"{sid},{cid},{score_str}\n")

    return marks
