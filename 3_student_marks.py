import math
import numpy as np
import curses


class Student:
    '''Added attribut marks and credit to simplify'''
    def __init__(self, data):
        self.id = int(data[0])
        self.name = data[1]
        self.dob = data[2]
        self.marks = {}    
        self.credits = {}   

    def __str__(self):
        '''no change'''
        return f"Id = {self.id}\nName = {self.name}\nDate of Birth = {self.dob}\nGPA = {self.calculate_gpa():.2f}\n"

    @staticmethod
    def Create_tab(n):
        '''no change (still one line)'''
        return { (info := input("Enter Id Name Date: ").split())[0] : Student(info) for _ in range(n) }

    def calculate_gpa(self):
        '''new function to calculate the gpa'''
        if not self.marks:
            return 0.0
        weighted_scores = []
        total_credits = []
        for cid, scores in self.marks.items():
            avg_score = np.mean(scores)        # moyenne des notes du cours fais avec numpy
            credit = self.credits[cid]         
            gpa_score = (avg_score / 20) * 4   # conversion sur 4
            weighted_scores.append(gpa_score * credit)
            total_credits.append(credit)
        return sum(weighted_scores)/sum(total_credits)

class Courses:
    def __init__(self, data):
        self.id = int(data[0])
        self.name = data[1]
        self.credit = 2   # default

    def __str__(self):
        '''no change'''
        return f"Id = {self.id}\nName = {self.name}\nCredits = {self.credit}\n"

    @staticmethod
    def create_tab(n):
        '''no change (still one line)'''
        return { int((info := input("Enter course info (Id Name): ").split())[0]) : Courses(info) for _ in range(n) }


class Marks:
    def __init__(self):
        self.tab_marks = {}

    def create_tab(self, tab_students, tab_courses):
        '''change to get the marks in input and calculate the floor'''
        for cid, course in tab_courses.items():
            for sid, student in tab_students.items():
                while True:
                    raw = input(f"Enter marks for {student.name} in {course.name} (separated by space): ")
                    parts = raw.split()
                    try:
                        scores = [math.floor(float(x)*10)/10 for x in parts]  # arrondi 1 décimale
                        break
                    except ValueError:
                        print("Please enter numeric scores separated by spaces.")
                
                student.marks[cid] = scores
                student.credits[cid] = course.credit  


#display with module curses
def display_sorted_students(tab_students):
    '''utilise curses afin d avoir un beau UI'''
    sorted_list = sorted(tab_students.values(), key=lambda s: s.calculate_gpa(), reverse=True)

    def ui(screen):
        '''aider par internet'''
        screen.clear()
        screen.addstr(0, 0, "=== Students sorted by GPA ===")
        for i, s in enumerate(sorted_list, start=2):
            screen.addstr(i, 0, f"{s.name} | GPA = {s.calculate_gpa():.2f}")
        screen.refresh()
        screen.getch()

    curses.wrapper(ui)



def main():
    '''creation of student, courses and marks and calculate the gpa of 
    each student.'''
    n = int(input("How many students? "))
    students = Student.Create_tab(n)

    c = int(input("How many courses? "))
    courses = Courses.create_tab(c)

    marks = Marks()
    marks.create_tab(students, courses)

    display_sorted_students(students)

    print("\n=== Final Students ===")
    for s in students.values():
        print(s)

if __name__ == "__main__":
    main()