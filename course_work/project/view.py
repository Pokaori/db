import datetime
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rc('xtick',labelsize=8)

class View:

    def print_menu(self):
         choice = -1
         while not (choice in range(61)):
             print("Select an option")
             print("1. Find a student by name")
             print("2. Find a student by id")
             print("3. Find a teacher by name")
             print("4. Find a teacher by id ")
             print("5. Find a subject by name")
             print("6. Find a subject by id")
             print("7. Find a faculty by name")
             print("8. Find a faculty by id")
             print("9. Find a department by name")
             print("10. Find a department by id")
             print("11. Find a faculty_department by id")
             print("12. Find a score by id")
             print("13. Find student`s scores ")
             print("14. Find teacher`s subjects")
             print("15. Find student`s subjects")
             print("16. Find all students")
             print("17. Find all teachers")
             print("18. Find all subjects")
             print("19. Find all scores")
             print("20. Find all faculty_department")
             print("21. Find all faculties")
             print("22. Find all departments")
             print("23. Add a student")
             print("24. Add a teacher")
             print("25. Add a subject ")
             print("26. Add a score")
             print("27. Add a fac_dep")
             print("28. Add a faculty")
             print("29. Add a department")
             print("30. Update a student")
             print("31. Update a teacher")
             print("32. Update a subject ")
             print("33. Update a score")
             print("34. Update a fac_dep")
             print("35. Update a faculty")
             print("36. Update a department")
             print("37. Remove a student")
             print("38. Remove a teacher")
             print("39. Remove a subject ")
             print("40. Remove a score")
             print("41. Remove a fac_dep")
             print("42. Remove a faculty")
             print("43. Remove a department")
             print("44. Find faculty_department and study_form where faculty and name like some text and price less some number ")
             print("45. Find student where name like some text, semester is some number and min score less than some number")
             print("46. Find teacher, faculty, subject where faculty, teacher and subject like some text")
             print("47. Find faculty, subject, average score where faculty and subject like some text and average score is between some numbers")
             print("48. Find student`s subjects for current semester where faculty and department name is some text,student name like and  current semester is   ")
             print("49. Generate faculty_department ")
             print("50. Generate scores")
             print("51. Generate subjects")
             print("52. Generate students")
             print("53. Generate teachers")
             print("54. Generate faculties")
             print("55. Generate departments")
             print("56. Average price of departments")
             print("57. Student scores and subjects")
             print("58. Count teachers`s subjects on faculty")
             print("59. Count teachers on positions on faculty")
             print("60. Exit ")
             try:
                choice =  int(input ("Enter your choice:"))
             except Exception:
                 continue
         return str(choice)

    def get_id(self):
        id=0
        while True:
            try:
                id=int(input("Enter id:"))
                if id<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return id

    def get_name(self):
        return input("Enter name:")

    def get_date(self):
        while True:
            try:
                year = int(input("Enter year:"))
                month = int(input("Enter month:"))
                day = int(input("Enter day: "))
                if (year<1)  or (month<1) or (day<1) :
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            try:
                date=datetime.date(year,month,day)
                break
            except ValueError as e:
                print(e)
        return date



    def add_student(self):
        student={}
        student["name"]=input("Enter full name:")
        print("Date of birth:")
        student["date_of_birth"] = self.get_date()
        print("Date of enter:")
        student["date_enter"] = self.get_date()
        while True:
            try:
                student["phone"] = int(input("Enter phone:"))
                if student["phone"]<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        student["phone"] = '+'+ str(student["phone"])
        student["email"] = input("Enter email:")
        while True:
            student["form_payment"]=input("Enter form of payment Budget or Contract:")
            if(student["form_payment"]!="Budget" and student["form_payment"]!="Contract"):
                print("You should enter Budget or Contract. Try again")
                continue
            break
        while True:
            try:
                student["semester"]=int(input("Enter semester(1,12):"))
                if student["semester"]<1 or student["semester"]>12:
                    print("You must enter integer in range(1,12). Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            student["gender"]=input("Enter gender M or F:")
            if(student["gender"]!="M" and student["gender"]!="F"):
                print("You should enter M or F. Try again")
                continue
            break
        while True:
            try:
                student["id_fac_dep"]=int(input("Enter id_fac_dep:"))
                if student["id_fac_dep"]<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return student

    def add_teacher(self):
        teacher={}
        teacher["name"] = input("Enter full name:")
        print("Date of birth:")
        teacher["date_of_birth"] = self.get_date()
        while True:
            try:
                teacher["from_year"]=int(input("Enter from which year work:"))
                if teacher["from_year"]<1 or teacher["from_year"]>2020:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter year. Try again")
                continue
            break
        while True:
            teacher["position"]=input("Enter position Assistance,Head teacher,Docent or Professor:")
            if(teacher["position"]!="Assistance" and  teacher["position"]!="Head teacher" and teacher["position"]!="Docent" and  teacher["position"]!="Professor"):
                print("You should enter Assistance,Head teacher,Docent or Professor. Try again")
                continue
            break
        while True:
            try:
                teacher["phone"] = int(input("Enter phone:"))
                if teacher["phone"]<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        teacher["phone"] = '+'+ str(teacher["phone"])
        teacher["email"] = input("Enter email:")
        while True:
            teacher["gender"]=input("Enter gender M or F:")
            if(teacher["gender"]!="M" and teacher["gender"]!="F"):
                print("You should enter M or F. Try again")
                continue
            break
        return teacher

    def add_subject(self):
        subject={}
        subject["name"] = input("Enter name:")
        while True:
            try:
                subject["semester"]=int(input("Enter semester(1,12):"))
                if subject["semester"]<1 or subject["semester"]>12:
                    print("You must enter integer in range(1,12). Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            try:
                subject["id_teacher"]=int(input("Enter id teacher:"))
                if subject["id_teacher"]<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            try:
                subject["id_fac_dep"]=int(input("Enter id_fac_dep:"))
                if subject["id_fac_dep"]<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return subject

    def add_score(self):
        score={}
        while True:
            try:
                score["score"]=int(input("Enter score(0,100):"))
                if score["score"]<0 or score["score"]>100:
                    print("You must enter integer in range(0,100). Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            try:
                score["id_subject"]=int(input("Enter id subject:"))
                if score["id_subject"]<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            try:
                score["id_student"]=int(input("Enter id student:"))
                if score["id_student"]<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return score

    def add_faculty(self):
        faculty={}
        faculty["name"] = input("Enter name:")
        faculty["name_dean"] = input("Enter name of dean:")
        faculty["adress"] = input("Enter adress:")
        while True:
            try:
                faculty["phone"] = int(input("Enter phone:"))
                if faculty["phone"]<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        faculty["phone"] = '+' + str(faculty["phone"])
        faculty["email"] = input("Enter email:")
        faculty["description"] = input("Enter description:")
        return faculty

    def add_department(self):
        department={}
        department["name"] = input("Enter name:")
        while True:
            department["study_form"]=input("Enter form of payment Daytime or Extramural:")
            if(department["study_form"]!="Daytime" and department["study_form"]!="Extramural"):
                print("You should enter Daytime or Extramural. Try again")
                continue
            break
        department["description"] = input("Enter description:")
        return department

    def add_fac_dep(self):
        fac_dep={}
        while True:
            try:
                fac_dep["price"] = int(input("Enter price:"))
                if fac_dep["price"]<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            try:
                fac_dep["id_fac"]=int(input("Enter id faculty:"))
                if fac_dep["id_fac"]<1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            try:
                fac_dep["id_dep"]=int(input("Enter id department:"))
                if fac_dep["id_dep"]:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        fac_dep["hame_head"]=input("Enter name of head:")
        return fac_dep

    def update_student(self):
        student = {}
        student["name"] = input("Enter full name or nothing:")
        while True:
            try:
                student["phone"] = int(input("Enter phone or 0:"))
                if student["phone"] < 0:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        if(student["phone"]!=0):
            student["phone"] = '+' + str(student["phone"])
        student["email"] = input("Enter email or nothing:")
        while True:
            student["form_payment"] = input("Enter form of payment Budget or Contract or nothing:")
            if (student["form_payment"] != "Budget" and student["form_payment"] != "Contract" and student["form_payment"] != ""):
                print("You should enter Budget or Contract or nothing. Try again")
                continue
            break
        while True:
            try:
                student["semester"] = int(input("Enter semester(1,12) or 0:"))
                if student["semester"] < 0 or student["semester"] > 12:
                    print("You must enter integer in range(1,12) or 0. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            try:
                student["id_fac_dep"] = int(input("Enter id_fac_dep or 0:"))
                if student["id_fac_dep"] < 0:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return student

    def update_teacher(self):
        teacher = {}
        teacher["name"] = input("Enter full name or nothing:")
        while True:
            teacher["position"] = input("Enter position Assistance,Head teacher,Docent or Professor or nothing:")
            if (teacher["position"] != "Assistance" and teacher["position"] != "Head teacher" and teacher[
                "position"] != "Docent" and teacher["position"] != "Professor" and teacher["position"] != ""):
                print("You should enter Assistance,Head teacher,Docent or Professor or nothing. Try again")
                continue
            break
        while True:
            try:
                teacher["phone"] = int(input("Enter phone or 0:"))
                if teacher["phone"] < 0:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        if(teacher["phone"]!=0):
            teacher["phone"] = '+' + str(teacher["phone"])
        teacher["email"] = input("Enter email or nothing:")
        return teacher

    def update_subject(self):
        subject = {}
        subject["name"] = input("Enter name or nothing:")
        while True:
            try:
                subject["id_teacher"] = int(input("Enter id teacher or 0:"))
                if subject["id_teacher"] < 0:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return subject

    def update_score(self):
        score = {}
        while True:
            try:
                score["score"] = int(input("Enter score(0,100):"))
                if score["score"] < 0 or score["score"] > 100:
                    print("You must enter integer in range(0,100) . Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return score

    def update_faculty(self):
        faculty = {}
        faculty["name"] = input("Enter name or nothing:")
        faculty["name_dean"] = input("Enter name of dean or nothing:")
        faculty["adress"] = input("Enter adress or nothing:")
        while True:
            try:
                faculty["phone"] = int(input("Enter phone or 0:"))
                if faculty["phone"] < 0:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        if(faculty["phone"]!=0):
            faculty["phone"] = '+' + str(faculty["phone"])
        faculty["email"] = input("Enter email or nothing:")
        faculty["description"] = input("Enter description or nothing:")
        return faculty

    def update_department(self):
        department = {}
        department["name"] = input("Enter name or nothing:")
        while True:
            department["study_form"] = input("Enter form of payment Daytime or Extramural or nothing:")
            if (department["study_form"] != "Daytime" and department["study_form"] != "Extramural" and department["study_form"] != ""):
                print("You should enter Daytime or Extramural or nothing. Try again")
                continue
            break
        department["description"] = input("Enter description or nothing:")
        return department

    def update_fac_dep(self):
        fac_dep = {}
        while True:
            try:
                fac_dep["price"] = int(input("Enter price or 0:"))
                if fac_dep["price"] < 0:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        fac_dep["hame_head"] = input("Enter name of head or nothing:")
        return fac_dep

    def get_edu_price_less_faculty_department(self):
        result={}
        while True:
            try:
                result["price"] = int(input("Enter price :"))
                if result["price"] < 1:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        result["faculty"] = input("Enter faculty name:")
        result["department"] = input("Enter department name:")
        return result

    def print_edu_price_less_faculty_department(self,edus):
        for edu in edus:
            print("Faculty: ", edu.fac_name)
            print("Department:",edu.dep_name)
            print("Study form: ",edu.study_form)
            print(" ")

    def get_students_name_semester_score_less(self):
        result={}
        result["name"] = input("Enter name:")
        while True:
            try:
                result["semester"]=int(input("Enter semester(1,12):"))
                if result["semester"]<1 or result["semester"]>12:
                    print("You must enter integer in range(1,12). Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            try:
                result["score"] = int(input("Enter score(0,100):"))
                if result["score"] < 0 or result["score"] > 100:
                    print("You must enter integer in range(0,100) . Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return result

    def print_students_name_semester_score_less(self,reses):
        for res in reses:
            print("Student name:",res.name)
            print("Min score:", res.min)
            print(" ")

    def get_teacher_subject_faculty(self):
        result={}
        result["faculty"] = input("Enter faculty name:")
        result["subject"] = input("Enter subject name:")
        result["teacher"] = input("Enter teacher name:")
        return result

    def print_teacher_subject_faculty(self,reses):
        for res in reses:
            print("Teacher name:",res.te_name)
            print("Subject name:", res.sub_name)
            print("Faculty name: ", res.fac_name)
            print(" ")

    def get_faculty_subject_score_between(self):
        result={}
        result["faculty"] = input("Enter faculty name:")
        result["subject"] = input("Enter subject name:")
        while True:
            try:
                result["score1"] = int(input("Enter score 1 (0,100):"))
                if result["score1"] < 0 or result["score1"] > 100:
                    print("You must enter integer in range(0,100) . Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        while True:
            try:
                result["score2"] = int(input("Enter score 2 (0,100):"))
                if result["score2"] < 0 or result["score2"] > 100:
                    print("You must enter integer in range(0,100) . Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return result

    def print_faculty_subject_score_between(self,reses):
        for res in reses:
            print("Faculty name:", res[0])
            print("Subject name:", res[1])
            print("Average score:", res[2])
            print(" ")

    def get_student_subjects_on_fac_dep_semester(self):
        result = {}
        result["faculty"] = input("Enter faculty name:")
        result["department"] = input("Enter department name:")
        result["student"] = input("Enter student name:")
        while True:
            try:
                result["semester"]=int(input("Enter semester(1,12):"))
                if result["semester"]<1 or result["semester"]>12:
                    print("You must enter integer in range(1,12). Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return result

    def print_student_subjects_on_fac_dep_semester(self,reses):
        for res in reses:
            print("Student name: ",res.stu_name)
            print("Subject name: ", res.sub_name)
            print(" ")

    def print_entities(self,entities):
        for entity in entities:
            print(entity)

    def print_entity(self,entity):
        print(entity)

    def get_number_generate(self):
        number=0
        while True:
            try:
                number=int(input("Enter number for generate:"))
                if number<0:
                    print("You must enter positive integer. Try again")
                    continue
            except ValueError:
                print("You should enter integer. Try again")
                continue
            break
        return number

    def print_mes(self, mes):
        print(mes)

    def get_form_study(self):
        while True:
            form_study=input("Enter form of payment Daytime or Extramural:")
            if(form_study!="Daytime" and form_study!="Extramural"):
                print("You should enter Daytime or Extramural. Try again")
                continue
            break
        return form_study

    def get_name_student(self):
        name = input("Enter full student name:")
        return name

    def get_faculty(self):
        faculty = input("Enter faculty name:")
        return faculty

    def show_plot_bar(self,entity):
        entity.plot.bar()
        plt.show()
