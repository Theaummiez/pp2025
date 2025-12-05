from domains.student import Student
from domains.courses import Courses
from domains.marks import Marks

from input import input_students, input_courses, input_marks
from output import display_sorted_students

def main():
    students = input_students(Student)
    courses = input_courses(Courses)
    marks = input_marks(students, courses, Marks)

    display_sorted_students(students)

    print("\n=== Final Students ===")
    for s in students.values():
        print(s)

if __name__ == "__main__":
    main()
