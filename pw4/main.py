from domains import Student, Courses, Marks
from input import get_input
from output import display_sorted_students


def main():
    print("=== Student GPA System ===")

    # Create students
    n = int(get_input("How many students? "))
    students = Student.create_tab(n, get_input)

    # Create courses
    c = int(get_input("How many courses? "))
    courses = Courses.create_tab(c, get_input)

    # Create marks
    marks = Marks()
    marks.create_tab(students, courses, get_input)

    # Display sorted GPA
    display_sorted_students(students)

    # Print final student catalogue
    print("\n=== Final Students ===")
    for s in students.values():
        print(s)


if __name__ == "__main__":
    main()
