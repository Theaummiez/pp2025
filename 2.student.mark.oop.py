
class Student:
    def __init__(self,data):
        self.id = int(data[0])
        self.name = data[1]
        self.dob = data[2]

    def __str__(self):
        return f"Id = {self.id}\nName ={self.name}\nDate of Birth ={self.dob}\n"
    
    # very disgusting but does works
    @staticmethod
    def Create_tab(n):
        return { (info := input("Enter Id Name Date: ").split())[0] : Student(info) for _ in range(n) }

class Courses:
    def __init__(self,data):
        self.id = int(data[0])
        self.name = data[1]
    def __str__(self):
        return f"Id = {self.id}\nName ={self.name}\n"
    
    #same as student.create_tab but for courses
    @staticmethod
    def create_tab(n):
        return { int((info := input("Enter course info (Id Name): ").split())[0]) : Courses(info) for _ in range(n) }

class Marks:
    def __init__(self):
        self.tab_marks = {}

    def create_tab(self, tab_student, tab_courses):
        self.tab_marks = {
            tab_courses[cid].name: {tab_student[sid].name: [] for sid in tab_student}
            for cid in tab_courses
        }

def test():
    #create by chatgpt to test my code !!!
    # ---- Test Student ----
    s = Student(["1", "Alice", "12/12/2000"])
    print(s)

    # ---- Test Student.Create_tab ----
    import builtins

    inputs = iter(["1 Alice 12/12/2000", "2 Bob 11/11/2001"])
    real_input = builtins.input
    builtins.input = lambda _: next(inputs)
    tab_student = Student.Create_tab(2)
    builtins.input = real_input

    print("\nStudents table:")
    for s in tab_student.values():
        print(s)

    # ---- Test Courses.create_tab ----
    inputs = iter(["1 Math", "2 Python"])
    builtins.input = lambda _: next(inputs)
    tab_courses = Courses.create_tab(2)
    builtins.input = real_input

    print("Courses table:")
    for c in tab_courses.values():
        print(c)

    # ---- Test Marks ----
    m = Marks()
    m.create_tab(tab_student, tab_courses)

    print("Marks table:")
    print(m.tab_marks)

