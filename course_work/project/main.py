from database import DB
from view import View
from models import Student, Teacher, Department, Faculty, Fac_dep, Score, Subject

database = DB()
database.open()

view = View()
choice=0

while choice!='60':
    choice=view.print_menu()
    if choice=='1':
        name = view.get_name()
        students = database.find_student(name)
        if type(students) is str:
            view.print_mes(students)
        else:
            view.print_entities(students)
            view.print_mes("Find is successful")
    if choice=='2':
        id = view.get_id()
        student = database.find_student_by_id(id)
        if type(student) is str:
            view.print_mes(student)
        else:
            view.print_entity(student)
            view.print_mes("Find is successful")
    if choice=='3':
        name = view.get_name()
        teachers = database.find_teacher(name)
        if type(teachers) is str:
            view.print_mes(teachers)
        else:
            view.print_entities(teachers)
            view.print_mes("Find is successful")
    if choice=='4':
        id = view.get_id()
        teacher = database.find_teacher_by_id(id)
        if type(teacher) is str:
            view.print_mes(teacher)
        else:
            view.print_entity(teacher)
            view.print_mes("Find is successful")
    if choice=='5':
        name = view.get_name()
        subjects = database.find_subject(name)
        if type(subjects) is str:
            view.print_mes(subjects)
        else:
            view.print_entities(subjects)
            view.print_mes("Find is successful")
    if choice=='6':
        id = view.get_id()
        subject = database.find_subject_by_id(id)
        if type(subject) is str:
            view.print_mes(subject)
        else:
            view.print_entity(subject)
            view.print_mes("Find is successful")
    if choice=='7':
        name = view.get_name()
        faculties = database.find_faculty(name)
        if type(faculties) is str:
            view.print_mes(faculties)
        else:
            view.print_entities(faculties)
            view.print_mes("Find is successful")
    if choice=='8':
        id = view.get_id()
        faculty = database.find_faculty_by_id(id)
        if type(faculty) is str:
            view.print_mes(faculty)
        else:
            view.print_entity(faculty)
            view.print_mes("Find is successful")
    if choice=='9':
        name = view.get_name()
        departments = database.find_department(name)
        if type(departments) is str:
            view.print_mes(departments)
        else:
            view.print_entities(departments)
            view.print_mes("Find is successful")
    if choice=='10':
        id = view.get_id()
        department = database.find_department_by_id(id)
        if type(department) is str:
            view.print_mes(department)
        else:
            view.print_entity(department)
            view.print_mes("Find is successful")
    if choice=='11':
        id = view.get_id()
        fac_dep = database.find_fac_dep_by_id(id)
        if type(fac_dep) is str:
            view.print_mes(fac_dep)
        else:
            view.print_entity(fac_dep)
            view.print_mes("Find is successful")
    if choice=='12':
        id = view.get_id()
        score = database.find_score_by_id(id)
        if type(score) is str:
            view.print_mes(score)
        else:
            view.print_entity(score)
            view.print_mes("Find is successful")
    if choice=='13':
        id = view.get_id()
        scores = database.find_student_scores(id)
        if type(scores) is str:
            view.print_mes(scores)
        else:
            view.print_entities(scores)
            view.print_mes("Find is successful")
    if choice=='14':
        id = view.get_id()
        subjects = database.find_teacher_subjects(id)
        if type(subjects) is str:
            view.print_mes(subjects)
        else:
            view.print_entities(subjects)
            view.print_mes("Find is successful")
    if choice=='15':
        id = view.get_id()
        subjects = database.find_student_subjects(id)
        if type(subjects) is str:
            view.print_mes(subjects)
        else:
            view.print_entities(subjects)
            view.print_mes("Find is successful")
    if choice == '16':
        students = database.find_all_students()
        if type(students) is str:
            view.print_mes(students)
        else:
            view.print_entities(students)
            view.print_mes("Find is successful")
    if choice == '17':
        teachers = database.find_all_teachers()
        if type(teachers) is str:
            view.print_mes(teachers)
        else:
            view.print_entities(teachers)
            view.print_mes("Find is successful")
    if choice == '18':
        subjects = database.find_all_subjects()
        if type(subjects) is str:
            view.print_mes(subjects)
        else:
            view.print_entities(subjects)
            view.print_mes("Find is successful")
    if choice == '19':
        scores = database.find_all_scores()
        if type(scores) is str:
            view.print_mes(scores)
        else:
            view.print_entities(scores)
            view.print_mes("Find is successful")
    if choice == '20':
        fac_dep = database.find_all_fac_dep()
        if type(fac_dep) is str:
            view.print_mes(fac_dep)
        else:
            view.print_entities(fac_dep)
            view.print_mes("Find is successful")
    if choice == '21':
        faculties = database.find_all_faculties()
        if type(faculties) is str:
            view.print_mes(faculties)
        else:
            view.print_entities(faculties)
            view.print_mes("Find is successful")
    if choice == '22':
        departments = database.find_all_departments()
        if type(departments) is str:
            view.print_mes(departments)
        else:
            view.print_entities(departments)
            view.print_mes("Find is successful")
    if choice == '23':
        stu=view.add_student()
        student=Student(
        name=stu["name"],
        date_of_birth = stu["date_of_birth"],
        date_enter = stu["date_enter"],
        phone = stu["phone"],
        email = stu["email"],
        form_payment = stu["form_payment"],
        semester = stu["semester"],
        gender = stu["gender"],
        id_fac_dep = stu["id_fac_dep"]
        )
        mes=database.add_student(student)
        view.print_mes(mes)
    if choice == '24':
        stu=view.add_teacher()
        teacher=Teacher(
        name=stu["name"],
        date_of_birth = stu["date_of_birth"],
        from_year = stu["from_year"],
        position =stu["position"],
        phone = stu["phone"],
        email = stu["email"],
        gender = stu["gender"],
        )
        mes=database.add_teacher(teacher)
        view.print_mes(mes)
    if choice == '25':
        stu=view.add_subject()
        subject= Subject(
        name=stu["name"],
        semester= stu["semester"],
        id_teacher = stu["id_teacher"],
        id_fac_dep = stu["id_fac_dep"]
        )
        mes=database.add_subject(subject)
        view.print_mes(mes)
    if choice == '26':
        stu=view.add_score()
        score = Score(
        score= stu["score"],
        id_subject = stu["id_subject"],
        id_student = stu["id_student"]
        )
        mes=database.add_score(score)
        view.print_mes(mes)
    if choice == '27':
        stu=view.add_fac_dep()
        fac_dep = Fac_dep(
        price= stu["price"],
        id_fac = stu["id_fac"],
        id_dep = stu["id_dep"],
        name_head = stu["name_head"]
        )
        mes=database.add_fac_dep(fac_dep)
        view.print_mes(mes)
    if choice == '28':
        stu=view.add_faculty()
        faculty = Faculty(
        name=stu["name"],
        name_dean = stu["name_dean"],
        adress = stu["adress"],
        phone = stu["phone"],
        email = stu["email"],
        description = stu["description"]
        )
        mes=database.add_faculty(faculty)
        view.print_mes(mes)
    if choice == '29':
        stu=view.add_department()
        department = Department(
        name=stu["name"],
        study_form = stu["study_form"],
        description = stu["description"]
        )
        mes=database.add_department(department)
        view.print_mes(mes)
    if choice == '30':
        id = view.get_id()
        student_old = database.find_student_by_id(id)
        if student_old is str:
            view.print_mes(student_old)
            continue
        stu = view.update_student()
        if not stu["name"]:
            stu["name"] = student_old.name
        if not stu["phone"]:
            stu["phone"] = student_old.phone
        if not stu["email"]:
            stu["email"] = student_old.email
        if not stu["form_payment"]:
            stu["form_payment"] = student_old.form_payment
        if not stu["semester"]:
            stu["semester"] = student_old.semester
        if not stu["id_fac_dep"]:
            stu["id_fac_dep"] = student_old.id_fac_dep
        student = Student(
            id=id,
            name=stu["name"],
            date_of_birth=student_old.date_of_birth,
            date_enter=student_old.date_enter,
            phone=stu["phone"],
            email=stu["email"],
            form_payment=stu["form_payment"],
            semester=stu["semester"],
            gender=student_old.gender,
            id_fac_dep=stu["id_fac_dep"]
        )
        mes = database.update_student(student)
        view.print_mes(mes)
    if choice == '31':
        id = view.get_id()
        teacher_old = database.find_teacher_by_id(id)
        if teacher_old is str:
            view.print_mes(teacher_old)
            continue
        stu = view.update_teacher()
        if not stu["name"]:
            stu["name"] = teacher_old.name
        if not stu["phone"]:
            stu["phone"] = teacher_old.phone
        if not stu["email"]:
            stu["email"] = teacher_old.email
        if not stu["position"]:
            stu["position"] = teacher_old.position
        teacher = Teacher(
            id=id,
            name=stu["name"],
            date_of_birth=teacher_old.date_of_birth,
            from_year=teacher_old.from_year,
            position=stu["position"],
            phone=stu["phone"],
            email=stu["email"],
            gender=teacher_old.gender,
        )
        mes = database.update_teacher(teacher)
        view.print_mes(mes)
    if choice == '32':
        id = view.get_id()
        subject_old = database.find_subject_by_id(id)
        if subject_old is str:
            view.print_mes(subject_old)
            continue
        stu = view.update_subject()
        if not stu["name"]:
            stu["name"] = subject_old.name
        if not stu["id_teacher"]:
            stu["id_teacher"] = subject_old.id_teacher
        subject = Subject(
            id=id,
            name=stu["name"],
            semester=subject_old.semester,
            id_teacher = stu["id_teacher"],
            id_fac_dep = subject_old.id_fac_dep
        )
        mes = database.update_subject(subject)
        view.print_mes(mes)
    if choice == '33':
        id = view.get_id()
        score_old = database.find_score_by_id(id)
        if score_old is str:
            view.print_mes(score_old)
            continue
        stu = view.update_score()
        score = Score(
            id=id,
            score=stu["score"],
            id_subject=score_old.id_subject,
            id_student=score_old.id_student
        )
        mes = database.update_score(score)
        view.print_mes(mes)
    if choice == '34':
        id = view.get_id()
        fac_dep_old = database.find_fac_dep_by_id(id)
        if fac_dep_old is str:
            view.print_mes(fac_dep_old)
            continue
        stu = view.update_fac_dep()
        if not stu["price"]:
            stu["price"] = fac_dep_old.price
        if not stu["name_head"]:
            stu["name_head"] = fac_dep_old.name_head
        fac_dep = Fac_dep(
            id=id,
            price=stu["price"],
            id_fac= fac_dep_old.id_fac,
            id_dep=fac_dep_old.id_dep,
            name_head=stu["name_head"]
        )
        mes = database.update_fac_dep(fac_dep)
        view.print_mes(mes)
    if choice == '35':
        id = view.get_id()
        faculty_old = database.find_faculty_by_id(id)
        if faculty_old is str:
            view.print_mes(faculty_old)
            continue
        stu = view.update_faculty()
        if not stu["name"]:
            stu["name"] = faculty_old.name
        if not stu["name_dean"]:
            stu["name_dean"] = faculty_old.name
        if not stu["adress"]:
            stu["adress"] = faculty_old.name
        if not stu["phone"]:
            stu["phone"] = faculty_old.phone
        if not stu["email"]:
            stu["email"] = faculty_old.email
        if not stu["description"]:
            stu["description"] = faculty_old.email
        faculty = Faculty(
            id=id,
            name=stu["name"],
            name_dean=stu["name_dean"],
            adress=stu["adress"],
            phone=stu["phone"],
            email=stu["email"],
            description=stu["description"]
        )
        mes = database.update_faculty(faculty)
        view.print_mes(mes)
    if choice == '35':
        id = view.get_id()
        faculty_old = database.find_faculty_by_id(id)
        if faculty_old is str:
            view.print_mes(faculty_old)
            continue
        stu = view.update_fac_dep()
        if not stu["name"]:
            stu["name"] = faculty_old.name
        if not stu["name_dean"]:
            stu["name_dean"] = faculty_old.name
        if not stu["adress"]:
            stu["adress"] = faculty_old.name
        if not stu["phone"]:
            stu["phone"] = faculty_old.phone
        if not stu["email"]:
            stu["email"] = faculty_old.email
        if not stu["description"]:
            stu["description"] = faculty_old.email
        faculty = Faculty(
            id=id,
            name=stu["name"],
            name_dean=stu["name_dean"],
            adress=stu["adress"],
            phone=stu["phone"],
            email=stu["email"],
            description=stu["description"]
        )
        mes = database.update_faculty(faculty)
        view.print_mes(mes)
    if choice == '36':
        id = view.get_id()
        department_old = database.find_department_by_id(id)
        if department_old is str:
            view.print_mes(department_old)
            continue
        stu = view.update_department()
        if not stu["name"]:
            stu["name"] = department_old.name
        if not stu["study_form"]:
            stu["study_form"] = department_old.study_form
        if not stu["description"]:
            stu["description"] = department_old.email
        department = Department(
        id=id,
        name=stu["name"],
        study_form = stu["study_form"],
        description = stu["description"]
        )
        mes = database.update_department(department)
        view.print_mes(mes)
    if choice == '37':
        id = view.get_id()
        student = database.find_student_by_id(id)
        if student is str:
            view.print_mes(student)
            continue
        mes = database.remove_student(id)
        view.print_mes(mes)
    if choice == '38':
        id = view.get_id()
        teacher = database.find_teacher_by_id(id)
        if teacher is str:
            view.print_mes(teacher)
            continue
        mes = database.remove_teacher(id)
        view.print_mes(mes)
    if choice == '39':
        id = view.get_id()
        subject = database.find_subject_by_id(id)
        if subject is str:
            view.print_mes(subject)
            continue
        mes = database.remove_subject(id)
        view.print_mes(mes)
    if choice == '40':
        id = view.get_id()
        score = database.find_score_by_id(id)
        if score is str:
            view.print_mes(score)
            continue
        mes = database.remove_score(id)
        view.print_mes(mes)
    if choice == '41':
        id = view.get_id()
        fac_dep = database.find_fac_dep_by_id(id)
        if fac_dep is str:
            view.print_mes(fac_dep)
            continue
        mes = database.remove_fac_dep(id)
        view.print_mes(mes)
    if choice == '42':
        id = view.get_id()
        faculty = database.find_faculty_by_id(id)
        if faculty is str:
            view.print_mes(faculty)
            continue
        mes = database.remove_faculty(id)
        view.print_mes(mes)
    if choice == '43':
        id = view.get_id()
        department = database.find_department_by_id(id)
        if department is str:
            view.print_mes(department)
            continue
        mes = database.remove_department(id)
        view.print_mes(mes)
    if choice=='44':
        res = view.get_edu_price_less_faculty_department()
        result = database.find_edu_price_less_faculty_department(res["price"],res["faculty"],res["department"])
        if type(result) is str:
            view.print_mes(result)
        else:
            view.print_edu_price_less_faculty_department(result)
            view.print_mes("Find is successful")
    if choice=='45':
        res = view.get_students_name_semester_score_less()
        result = database.find_students_name_semester_score_less(res["name"],res["semester"],res["score"])
        if type(result) is str:
            view.print_mes(result)
        else:
            view.print_students_name_semester_score_less(result)
            view.print_mes("Find is successful")
    if choice=='46':
        res = view.get_teacher_subject_faculty()
        result = database.find_teacher_subject_faculty (res["subject"],res["faculty"],res["teacher"])
        if type(result) is str:
            view.print_mes(result)
        else:
            view.print_teacher_subject_faculty (result)
            view.print_mes("Find is successful")
    if choice=='47':
        res = view.get_faculty_subject_score_between()
        result = database.find_faculty_subject_score_between(res["faculty"],res["subject"],res["score1"],res["score2"])
        if type(result) is str:
            view.print_mes(result)
        else:
            view.print_faculty_subject_score_between(result)
            view.print_mes("Find is successful")
    if choice=='48':
        res = view.get_student_subjects_on_fac_dep_semester()
        result = database.find_student_subjects_on_fac_dep_semester (res["faculty"],res["department"],res["student"], res["semester"])
        if type(result) is str:
            view.print_mes(result)
        else:
            view.print_student_subjects_on_fac_dep_semester(result)
            view.print_mes("Find is successful")
    if choice == '49':
        number = view.get_number_generate()
        mes=database.generate_fac_dep(number)
        view.print_mes(mes)
    if choice == '50':
        number = view.get_number_generate()
        mes=database.generate_score(number)
        view.print_mes(mes)
    if choice == '51':
        number = view.get_number_generate()
        mes=database.generate_subjects(number)
        view.print_mes(mes)
    if choice == '52':
        number = view.get_number_generate()
        mes=database.generate_students(number)
        view.print_mes(mes)
    if choice == '53':
        number = view.get_number_generate()
        mes=database.generate_teachers(number)
        view.print_mes(mes)
    if choice == '54':
        number = view.get_number_generate()
        mes=database.generate_faculties(number)
        view.print_mes(mes)
    if choice == '55':
        number = view.get_number_generate()
        mes=database.generate_departments(number)
        view.print_mes(mes)
    if choice =='56':
        form_study=view.get_form_study()
        res=database.filter_avg_price(form_study)
        view.show_plot_bar(res)
    if choice == '57':
        name = view.get_name_student()
        res=database.find_student_subjects_scores(name)
        view.show_plot_bar(res)
    if choice == '58':
        faculty =view.get_faculty()
        res=database.count_teacher_subjects(faculty)
        view.show_plot_bar(res)
    if choice == '59':
        faculty =view.get_faculty()
        res=database.count_teacher_position(faculty)
        view.show_plot_bar(res)


