#Student mark management

#table for student
def Create_table_student():
    '''Create a table: input the number of student then input th information
    Student : {ID: (name,DoB)}'''
    tab_student = {}
    nb_student = int(input("Enter the number of student:"))

    for i in range(nb_student):
        ID = int(input("Enter id of the student:" ))
        name = str(input("enter the name of the student:"))
        DoB = str(input("enter date pf birth (JJ/MM/YYYY)"))
        tab_student[ID] = (name,DoB)
    return tab_student

#table for courses
def Create_table_courses():
    '''Create a table: input the number of courses then input the information
    courses : {ID: name}'''
    tab_courses = {}
    nb_courses = int(input("Enter the number of Courses"))

    for _ in range(nb_courses):
        ID = int(input("Enter id of the course:" ))
        name = str(input("enter the name of the course:"))
        tab_courses[ID] = name
    return tab_courses

#table for marks
def Create_table_marks(Students:dict,Courses:dict):
    '''Create a table: input the number of courses then input the information
    marks : {courses_name: {student_name: {id_marks:marks}}}'''
    tab_mark = {}
    id_course = int(input("Enter the id of the course:"))
    if Courses[id_course] not in tab_mark:
        tab_mark[Courses[id_course]] = {}

    id_student = int(input("Enter the id of the student"))
    if Students[id_student] not in tab_mark[Courses[id_course]]:
        tab_mark[Courses[id_course]][Students[id_student]] = {}

    nb_marks = int(input("enter the number of mark of the student"))
    for i in range(nb_marks):
        mark = int(input("Enter the mark :"))
        tab_mark[Courses[id_course]][Students[id_student]][i] = mark
    return tab_mark

#add student to table student
def Add_student(Student:dict):
    '''Add input in table student '''
    ID = int(input("Enter id of the student:" ))
    name = str(input("enter the name of the student:"))
    DoB = str(input("enter date pf birth (JJ/MM/YYYY)"))
    if ID not in Student:
        Student[ID] = (name,DoB)
    else:
        print("Id already existing")
        return Student
    return Student

#add courses to table courses
def Add_course(Courses:dict):
    '''add courses in table courses'''
    ID = int(input("Enter id of the course:" ))
    name = str(input("enter the name of the course:"))
    if ID not in Courses:
        Courses[ID] = name
    else:
        print("Id already exist")
        return Courses
    return Courses

#add marks to table marks
def Add_marks(Marks:dict, Courses:dict, Student:dict):
    '''add marks in a specific courses for a specific student'''
    id_course = int(input("Enter the id of the course:"))
    if id_course not in Courses:
        print("Course id not found")
        return Marks

    id_student = int(input("Enter the id of the student:"))
    if id_student not in Student:
        print("Student id not found")
        return Marks

    course_name = Courses[id_course]
    student_name = Student[id_student][0]

    if course_name not in Marks:
        Marks[course_name] = {}

    if student_name not in Marks[course_name]:
        Marks[course_name][student_name] = {}

    mark = int(input("Enter the note:"))
    student_marks = Marks[course_name][student_name]
    next_key = len(student_marks) + 1
    student_marks[next_key] = mark

    return Marks

#display table courses
def DisplayC(Courses:dict):
    '''Display table courses'''
    print("Courses:")
    for key, name in Courses.items():
        print(f"id   :{key} \nname :{name}\n")

#display table student
def DipslayS(Student:dict):
    '''Display table Student'''
    print("Students:")
    for key, info in Student.items():
        print(f"id   :{key} \nname :{info[0]}\nDate of Birth :{info[1]}\n")

#display table marks
def DisplayM(Marks:dict):
    '''Display table marks'''
    for courses , student in Marks.items():
        print(f"For student {list(student.keys())} in courses {courses}")
        for n, marks in student.items():
            print(f"{n} Exams : {marks}")

#test the function    
def test():
    '''Test all function'''
    Tab_test_student = {
        1:("tomy","12/12/1212"),
        2:("Nam", "13/12/2332")
        }

    Tab_test_courses = {
        1:"Math",
        2:"SQL",
        3:"DSA"
        }

    Tab_test_marks = { 
        "Math":{
            "tomy":{1:12,2:13,3:14},
            "Nam":{1:12,2:13,3:14}
        },
        "SQL":{
            "Mich":{1:12,2:13,3:14},
            "Nam":{1:12,2:13,3:14}
        }
    }

    #DisplayC(Tab_test_courses)
    #DipslayS(Tab_test_student)
    #DisplayM(Tab_test_marks)

    print("Befor change")
    DisplayM(Tab_test_marks)
    Table_marks = Add_marks(Tab_test_marks, Tab_test_courses, Tab_test_student)
    print("after change")
    DisplayM(Tab_test_marks)

