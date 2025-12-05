import os
from compression import decompress_data, compress_data
from domains.student import Student
from domains.courses import Courses
from domains.marks import Marks
from input import input_students, input_courses, input_marks
from output import display_sorted_students

def load_or_create_data():
    print("Checking for compressed archive...")

    archive_exists = decompress_data()

    students = {}
    courses = {}
    marks = Marks()

    if archive_exists:
        print("Loading data from extracted text files...")

        # Load students.txt
        if os.path.exists("students.txt"):
            with open("students.txt") as f:
                for line in f:
                    sid, name, dob = line.strip().split(",")
                    students[sid] = Student([sid, name, dob])

        # Load courses.txt
        if os.path.exists("courses.txt"):
            with open("courses.txt") as f:
                for line in f:
                    cid, name = line.strip().split(",")
                    courses[int(cid)] = Courses([cid, name])

        # Load marks.txt
        if os.path.exists("marks.txt"):
            with open("marks.txt") as f:
                for line in f:
                    sid, cid, *scores = line.strip().split(",")
                    scores = list(map(float, scores))

                    student = students[sid]
                    student.marks[int(cid)] = scores

        print("Data successfully loaded.\n")
    else:
        print("No archive found. Starting fresh.")
        students = input_students()
        courses = input_courses()
        marks = input_marks(students, courses)

        # Write data to text files
        write_text_files(students, courses, marks)

        # Compress them
        compress_data()

    return students, courses, marks


def write_text_files(students, courses, marks):
    # Students
    with open("students.txt", "w") as f:
        for s in students.values():
            f.write(f"{s.id},{s.name},{s.dob}\n")

    # Courses
    with open("courses.txt", "w") as f:
        for c in courses.values():
            f.write(f"{c.id},{c.name}\n")

    # Marks
    with open("marks.txt", "w") as f:
        for s in students.values():
            for cid, scores in s.marks.items():
                scores_str = ",".join(map(str, scores))
                f.write(f"{s.id},{cid},{scores_str}\n")


def main():
    students, courses, marks = load_or_create_data()

    display_sorted_students(students)

    print("\n=== Final Students ===")
    for s in students.values():
        print(s)

    print("\nCompressing data before exit...")
    compress_data()


if __name__ == "__main__":
    main()
