import math
import numpy as np

class Student:
    def __init__(self,n:str,i:int,d:str):
        self.s_name = n
        self.s_id = i
        self.dob = d
    
    def __str__(self):
        
        return f"Id : ICT0{self.s_id}\nName : {self.s_name}\nDate of birth : {self.dob}\n"


class Courses:
    def __init__(self,n:str,i:int,c:int):
        self.c_name = n
        self.c_id = i
        self.credit = c

    def __str__(self):
        return f"Id : {self.c_id}\nName : {self.c_name}\nCredits : {self.credit}"
    
class Marksmanagement(Student,Courses):
    def __init__(self):
        self.tab_student = []
        self.tab_courses = []
        self.dic_marks = {}
    
    def get_name_from_id_st(self,id):
        #get the name of the student from the id
        for stud in self.tab_student:
            if stud.s_id ==id:
                return stud.s_name
            
    def get_name_from_id_co(self,id):
        #get the name of the courses from the id
        for cours in self.tab_courses:
            if cours.c_id ==id:
                return cours.c_name
        
        
    def display_student(self):
        print("======Student=======")
        for elem in self.tab_student:
            print(elem)
    
    def display_courses(self):
        print("======Courses=======")
        for elem in self.tab_courses:
            print(elem)
    
    def display_marks(self):
        print("=====Marks=====")
        for IdC,val in self.dic_marks.items():

            cours_name = self.get_name_from_id_co(IdC)
            
            print(f"======{cours_name}=======")

            for Ids,grade in val.items():

                val = self.get_name_from_id_st(Ids)

                print(f"{val} : {grade}")


    def add_student(self):
        info = input("Enter the information of the student (name id date of birth):").split()
        S = Student(info[0],info[1],info[2])
        self.tab_student.append(S)

    def add_courses(self):
        info = input("Enter the information of the courses (name id credit):").split()
        C = Courses(info[0],info[1],info[2])
        self.tab_courses.append(C)
        self.dic_marks[info[1]] = {}
    
    def add_marks(self):
        print("Choose a courses to grade")
        print("Option of courses :")
        for elem in self.tab_courses:
            print(elem)
        cours = input("Which courses could you like to grade (id) ?")
        if not cours in self.dic_marks.keys():
            return "Courses Id not found"
        print("option of student")
        for elem in self.tab_student:
            print(elem)
        id_stud = input("Which student would you like to enter the grade (id)?")
        

        if not id_stud in [stud.s_id for stud in self.tab_student]:
            print("ici bas")
            return "Student Id not found"
        
        n = int(input("how many grades would u like to enter :"))
        print("enter the grade")
    
        self.dic_marks[cours][id_stud] = []
        for _ in range(n):
            self.dic_marks[cours][id_stud].append(int(input("->")))
            print(self.dic_marks)

    def Get_GPA(self):
        
        for cour, dic_stud in self.dic_marks.items():
            cour_name = self.get_name_from_id_co(cour)
            print(f"====GPA of {cour_name} ======")
            for stud, list_grade in dic_stud.items():
                stud_name = self.get_name_from_id_st(stud)
                print(f"Student {stud_name} :",end ="")
                mean_scores = np.mean(list_grade)
                print(f"{mean_scores/20*4:.2f}")



def main():

    Management = Marksmanagement()

    while True:
        print("\n" + "="*40)
        print("   STUDENT MARK MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add Student")
        print("2. Add Course")
        print("3. Input Marks")
        print("4. List Students")
        print("5. List Courses")
        print("6. Show Marks")
        print("7. Calculate GPA")
        print("8. Exit")

        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            Management.add_student()
        elif choice == '2':
            Management.add_courses()
        elif choice == '3':
            Management.add_marks()
        elif choice == '4':
            Management.display_student()
        elif choice == '5':
            Management.display_courses()
        elif choice == '6':
            Management.display_marks()
        elif choice == '7':
            Management.Get_GPA()
        elif choice == '8':
            print("bye bye!")
            break
        else:
            print("Invalid choice! Please try again.")
        

if __name__ == "__main__":
    main()