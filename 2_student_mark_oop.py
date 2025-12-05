
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

