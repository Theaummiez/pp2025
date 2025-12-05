from domains.student import Student
from domains.courses import Courses
from domains.marks import Marks

def input_students():
    n = int(input("How many students? "))
    return Student.Create_tab(n)

def input_courses():
    n = int(input("How many courses? "))
    return Courses.create_tab(n)

def input_marks(students, courses):
    marks = Marks()
    marks.create_tab(students, courses)
    return marks
