import psycopg2
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
from models import Student, Teacher, Department, Faculty, Fac_dep, Score, Subject
import pandas as pd

class DB:

    def __init__(self):
        self.s = None
        self._engine= None
        self._engine2 = None
        self.s2 =None
    def open(self):
        try:
            self._engine = create_engine('postgres+psycopg2://postgres:16072002p@localhost:5432/Course_work')
            self._engine2 = create_engine('postgres+psycopg2://postgres:16072002p@localhost:5433/Course_work')
            Session = sessionmaker(bind=self._engine)
            Session2 = sessionmaker(bind=self._engine2)
            self.s = Session()
            self.s2 = Session2()
            print("Connect")
        except (Exception, exc.SQLAlchemyError) as error:
            print("Can`t connect to data base", error)

    def close(self):
        self.s.close()

    def find_student(self, name):
        students=None
        try:
            students=self.s.query(Student).filter_by(name=name).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            students=self.s2.query(Student).filter_by(name=name).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_student():", error)
        if students:
            return students
        else:
            return "Can`t find student by name"

    def find_student_by_id(self, id):
        student = None
        try:
            student=self.s.query(Student).get(id)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            student=self.s2.query(Student).get(id)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_student_by_id():", error)
        if student:
            return student
        else:
            return "Can`t find student by id"

    def find_teacher(self, name):
        teachers= None
        try:
            teachers = self.s.query(Teacher).filter_by(name=name).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            teachers = self.s2.query(Teacher).filter_by(name=name).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            print("Error in find_teacher():", error)
        if teachers:
            return teachers
        else:
            return "Can`t find teachers by name"

    def find_teacher_by_id(self, id):
        teacher=None
        try:
            teacher = self.s.query(Teacher).get(id)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            teacher = self.s2.query(Teacher).get(id)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_teacher_by_id():", error)
        if teacher:
            return teacher
        else:
            return "Can`t find teacher by id"

    def find_subject(self, name):
        subjects =None
        try:
            subjects = self.s.query(Subject).filter_by(name=name).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            subjects = self.s2.query(Subject).filter_by(name=name).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_subject():", error)
        if subjects:
            return subjects
        else:
            return "Can`t find subject by name"

    def find_subject_by_id(self, id):
        student=None
        try:
            student = self.s.query(Student).get(id)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            student = self.s2.query(Student).get(id)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_subject_by_id():", error)
        if student:
            return student
        else:
            return "Can`t find subject by id"

    def find_faculty(self, name):
        faculties=None
        try:
            faculties = self.s.query(Faculty).filter_by(name=name).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            faculties = self.s2.query(Faculty).filter_by(name=name).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_faculty():", error)
        if faculties:
            return faculties
        else:
            return "Can`t find faculties by name"

    def find_faculty_by_id(self, id):
        faculty = None
        try:
            faculty = self.s.query(Faculty).get(id)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            faculty = self.s2.query(Faculty).get(id)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_faculty_by_id():", error)
        if faculty:
            return faculty
        else:
            return "Can`t find faculty by id"

    def find_department(self, name):
        departments=None
        try:
            departments = self.s.query(Department).filter_by(name=name).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            departments = self.s2.query(Department).filter_by(name=name).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_department():", error)
        if departments:
            return departments
        else:
            return "Can`t find departments by name"

    def find_department_by_id(self, id):
        department=None
        try:
            department = self.s.query(Department).get(id)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            department = self.s2.query(Department).get(id)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_department_by_id():", error)
        if department:
            return department
        else:
            return "Can`t find department by id"

    def find_fac_dep_by_id(self, id):
        fac_dep=None
        try:
            fac_dep = self.s.query(Fac_dep).get(id)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            fac_dep = self.s2.query(Fac_dep).get(id)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_fac_dep_by_id():", error)
        if fac_dep:
            return fac_dep
        else:
            return "Can`t find fac_dep by id"

    def find_score_by_id(self, id):
        score = None
        try:
            score = self.s.query(Score).get(id)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            score = self.s2.query(Score).get(id)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_score_by_id():", error)
        if score:
            return score
        else:
            return "Can`t find score by id"

    def find_student_scores(self, id_student):
        scores = None
        try:
            scores = self.s.query(Student).get(id_student).scores
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            scores = self.s2.query(Student).get(id_student).scores
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_student_scores():", error)
        if scores:
            return scores
        else:
            return "Can`t find student`s score"

    def find_teacher_subjects(self, id_teacher):
        subjects=None
        try:
            subjects = self.s.query(Teacher).get(id_teacher).subjects
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            subjects = self.s2.query(Teacher).get(id_teacher).subjects
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_teacher_subjects():", error)
        if subjects:
            return subjects
        else:
            return "Can`t find teacher`s subjects"

    def find_student_subjects(self, id_student):
        subjects = []
        try:
            scores = self.s.query(Score).filter_by(id_student=id_student).all()
            for score in scores:
                subjects.append(self.s.query(Subject).get(score.id_subject))
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            scores = self.s2.query(Score).filter_by(id_student=id_student).all()
            for score in scores:
                subjects.append(self.s2.query(Subject).get(score.id_subject))
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_student_subjects():", error)
        if subjects:
            return subjects
        else:
            return "Can`t find student`s subjects"

    def find_all_students(self):
        students=None
        try:
            students = self.s.query(Student).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            students = self.s2.query(Student).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_all_students():", error)
        if students:
            return students
        else:
            return "Can`t find students"

    def find_all_teachers(self):
        teachers=None
        try:
            teachers = self.s.query(Teacher).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            teachers = self.s2.query(Teacher).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_all_teachers():", error)
        if teachers:
            return teachers
        else:
            return "Can`t find teachers"

    def find_all_subjects(self):
        subjects=None
        try:
            subjects = self.s.query(Subject).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            subjects = self.s2.query(Subject).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_all_subjects():", error)
        if subjects:
            return subjects
        else:
            return "Can`t find subjects"

    def find_all_scores(self):
        scores = None
        try:
            scores = self.s.query(Score).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            scores = self.s2.query(Score).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_all_scores():", error)
        if scores:
            return scores
        else:
            return "Can`t find scores"

    def find_all_fac_dep(self):
        fac_dep = None
        try:
            fac_dep = self.s.query(Fac_dep).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            fac_dep = self.s2.query(Fac_dep).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_all_fac_dep():", error)
        if fac_dep:
            return fac_dep
        else:
            return "Can`t find fac_dep"

    def find_all_faculties(self):
        faculties = None
        try:
            faculties = self.s.query(Faculty).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            faculties = self.s2.query(Faculty).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_all_faculties():", error)
        if faculties:
            return faculties
        else:
            return "Can`t find faculties"

    def find_all_departments(self):
        departments = None
        try:
            departments = self.s.query(Department).all()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            departments = self.s2.query(Department).all()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_all_departments():", error)
        if departments:
            return departments
        else:
            return "Can`t find departments"

    def add_student(self, student):
        try:
            self.s.add(student)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.add(student)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in add_student():", error)
        return "Add is successful"

    def add_teacher(self, teacher):
        try:
            self.s.add(teacher)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.add(teacher)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in add_teacher():", error)
        return "Add is successful"

    def add_subject(self, subject):
        try:
            self.s.add(subject)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.add(subject)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in add_subject():", error)
        return "Add is successful"

    def add_score(self, score):
        scores = None
        try:
            scores = self.s.query(Fac_dep).filter_by(id_subject=score.id_subject).filter_by(id_student=score.id_student).first()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            scores = self.s2.query(Fac_dep).filter_by(id_subject=score.id_subject).filter_by(id_student=score.id_student).first()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in add_score() first step:", error)
        if scores:
            return "Can`t add"
        try:
            self.s.add(score)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.add(score)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in add_score():", error)
        return "Add is successful"

    def add_fac_dep(self, fac_dep):
        fac_deps = None
        try:
            fac_deps = self.s.query(Fac_dep).filter_by(id_dep=fac_dep.id_dep).filter_by(id_fac=fac_dep.id_fac).first()
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            fac_deps = self.s2.query(Fac_dep).filter_by(id_dep=fac_dep.id_dep).filter_by(id_fac=fac_dep.id_fac).first()
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in add_fac_dep() first step:", error)
        if fac_deps:
            return "Can`t add"
        try:
            self.s.add(fac_dep)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.add(fac_dep)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in add_fac_dep() second step:", error)
        return "Add is successful"

    def add_faculty(self, faculty):
        try:
            self.s.add(faculty)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.add(faculty)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in add_faculty():", error)
        return "Add is successful"

    def add_department(self, department):
        try:
            self.s.add(department)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.add(department)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in add_department():", error)
        return "Add is successful"

    def update_student(self,student):
        u = None
        try:
            u = self.s.query(Student).filter_by(id=student.id).update(
                {Student.name:student.name, Student.phone:student.phone, Student.email:student.email,
                 Student.form_payment:student.form_payment, Student.semester:student.semester,
                 Student.id_fac_dep:student.id_fac_dep})
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            u = self.s2.query(Student).filter_by(id=student.id).update(
                {Student.name:student.name, Student.phone:student.phone, Student.email:student.email,
                 Student.form_payment:student.form_payment, Student.semester:student.semester,
                 Student.id_fac_dep:student.id_fac_dep})
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in update_student():", error)
        if u:
            return "Update student is successful"
        else:
            return "Can`t update student"

    def update_teacher(self,teacher):
        u = None
        try:
            u = self.s.query(Teacher).filter_by(id=teacher.id).update(
                {Teacher.name:teacher.name, Teacher.position:teacher.position,Teacher.phone:teacher.phone,Teacher.email:teacher.email})
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            u = self.s2.query(Teacher).filter_by(id=teacher.id).update(
                {Teacher.name:teacher.name, Teacher.position:teacher.position,Teacher.phone:teacher.phone,Teacher.email:teacher.email})
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in update_teacher():", error)
        if u:
            return "Update teacher is successful"
        else:
            return "Can`t update teacher"

    def update_subject(self,subject):
        u = None
        try:
            u = self.s.query(Subject).filter_by(id=subject.id).update(
                {Subject.name:subject.name, Subject.id_teacher:subject.id_teacher})
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            u = self.s2.query(Subject).filter_by(id=subject.id).update(
                {Subject.name:subject.name, Subject.id_teacher:subject.id_teacher})
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in update_subject():", error)
        if u:
            return "Update subject is successful"
        else:
            return "Can`t update subject"

    def update_department(self,department):
        u = None
        try:
            u = self.s.query(Department).filter_by(id=department.id).update(
                {Department.name:department.name,Department.study_form:department.study_form,
                 Department.description:department.description})
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            u = self.s2.query(Department).filter_by(id=department.id).update(
                {Department.name:department.name,Department.study_form:department.study_form,
                 Department.description:department.description})
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in update_department():", error)
        if u:
            return "Update department is successful"
        else:
            return "Can`t update department"

    def update_faculty(self,faculty):
        u=None
        try:
            u = self.s.query(Faculty).filter_by(id=faculty.id).update(
                {Faculty.name:faculty.name, Faculty.name_dean:faculty.name_dean,Faculty.adress:faculty.adress,Faculty.phone:faculty.phone,
                 Faculty.email:faculty.email,
                 Faculty.description:faculty.description})
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            u = self.s2.query(Faculty).filter_by(id=faculty.id).update(
                {Faculty.name:faculty.name, Faculty.name_dean:faculty.name_dean,Faculty.adress:faculty.adress,Faculty.phone:faculty.phone,
                 Faculty.email:faculty.email,
                 Faculty.description:faculty.description})
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in update_faculty():", error)
        if u:
            return "Update faculty is successful"
        else:
            return "Can`t update faculty"


    def update_fac_dep(self,fac_dep):
        u=None
        try:
            u = self.s.query(Fac_dep).filter_by(id=fac_dep.id).update(
                { Fac_dep.price:fac_dep.price,Fac_dep.name_head:fac_dep.name_head})
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            u = self.s2.query(Fac_dep).filter_by(id=fac_dep.id).update(
                { Fac_dep.price:fac_dep.price,Fac_dep.name_head:fac_dep.name_head})
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in update_fac_dep():", error)
        if u:
            return "Update fac_dep is successful"
        else:
            return "Can`t update fac_dep"

    def update_score(self,score):
        u= None
        try:
            u = self.s.query(Score).filter_by(id=score.id).update({Score.score:score.score})
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            u = self.s2.query(Score).filter_by(id=score.id).update({Score.score:score.score})
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in update_score():", error)
        if u:
            return "Update score is successful"
        else:
            return "Can`t update score"

    def remove_student(self, id):
        student = self.find_student_by_id(id)
        if type(student) is not Student:
            return "Can`t find by id"
        try:
            self.s.delete(student)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.delete(student)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in remove_student():", error)
        return "Delete is successful"

    def remove_teacher(self, id):
        teacher = self.find_teacher_by_id(id)
        if type(teacher) is not Teacher:
            return "Can`t find by id"
        try:
            self.s.delete(teacher)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.delete(teacher)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in remove_post():", error)
        return "Delete is successful"

    def remove_subject(self, id):
        subject = self.find_subject_by_id(id)
        if type(subject) is not Subject:
            return "Can`t find by id"
        try:
            self.s.delete(subject)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.delete(subject)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in remove_subject():", error)
        return "Delete is successful"

    def remove_score(self, id):
        score = self.find_score_by_id(id)
        if type(score) is not Score:
            return "Can`t find by id"
        try:
            self.s.delete(score)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.delete(score)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in remove_score():", error)
        return "Delete is successful"

    def remove_faculty(self, id):
        faculty = self.find_faculty_by_id(id)
        if type(faculty) is not Faculty:
            return "Can`t find by id"
        try:
            self.s.delete(faculty)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.delete(faculty)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in remove_faculty():", error)
        return "Delete is successful"

    def remove_department(self, id):
        department = self.find_department_by_id(id)
        if type(department) is not Department:
            return "Can`t find by id"
        try:
            self.s.delete(department)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.delete(department)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in remove_department():", error)
        return "Delete is successful"

    def remove_fac_dep(self, id):
        fac_dep = self.find_fac_dep_by_id(id)
        if type(fac_dep) is not Fac_dep:
            return "Can`t find by id"
        try:
            self.s.delete(fac_dep)
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.delete(fac_dep)
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in remove_fac_dep():", error)
        return "Delete is successful"

    def find_edu_price_less_faculty_department(self,price,faculty,department):
        result=None
        try:
            result=self.s.execute(
                f"select faculties.name fac_name, departments.name dep_name, study_form from fac_dep inner join faculties on id_fac=faculties.id inner join departments on id_dep=departments.id where price<{price} and faculties.name like '%{faculty}%' and departments.name like '%{department}%';")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            result=self.s2.execute(
                f"select faculties.name fac_name, departments.name dep_name, study_form from fac_dep inner join faculties on id_fac=faculties.id inner join departments on id_dep=departments.id where price<{price} and faculties.name like '%{faculty}%' and departments.name like '%{department}%';")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_edu_price_less_faculty_department():", error)
        if not result:
            return "Can`t find"
        return result

    def find_students_name_semester_score_less(self,name,semester,score):
        result=None
        try:
            result=self.s.execute(
                f"select students.name, min(score) from scores inner join students on id_student=students.id inner join subjects on id_subject=subjects.id where subjects.semester={semester} and students.name like '%{name}%' group by students.name having min(score)<{score};")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            result=self.s2.execute(
                f"select students.name, min(score) from scores inner join students on id_student=students.id inner join subjects on id_subject=subjects.id where subjects.semester={semester} and students.name like '%{name}%' group by students.name having min(score)<{score};")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_students_name_semester_score_less():", error)
        if not result:
            return "Can`t find"
        return result

    def find_teacher_subject_faculty(self,subject,faculty,teacher):
        result = None
        try:
            result=self.s.execute(
                f"select teachers.name te_name, subjects.name sub_name,faculties.name fac_name from subjects inner join teachers on teachers.id=id_teacher inner join fac_dep on fac_dep.id=id_fac_dep inner join faculties on fac_dep.id_fac=faculties.id where faculties.name like '%{faculty}%' and subjects.name like '%{subject}%' and teachers.name like '%{teacher}%';")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            result=self.s2.execute(
                f"select teachers.name te_name, subjects.name sub_name,faculties.name fac_name from subjects inner join teachers on teachers.id=id_teacher inner join fac_dep on fac_dep.id=id_fac_dep inner join faculties on fac_dep.id_fac=faculties.id where faculties.name like '%{faculty}%' and subjects.name like '%{subject}%' and teachers.name like '%{teacher}%';")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_teacher_subject_faculty():", error)
        if not result:
            return "Can`t find"
        return result

    def find_faculty_subject_score_between(self,faculty,subject,score1,score2):
        result=None
        try:
            result=self.s.execute(
                f"select faculties.name fac_name , subjects.name sub_name, AVG(score) from subjects inner join scores on subjects.id=id_subject inner join fac_dep on fac_dep.id=id_fac_dep inner join faculties on fac_dep.id_fac=faculties.id where faculties.name like '%{faculty}%' and subjects.name like '%{subject}%' group by faculties.name, subjects.name having AVG(score) between {score1} and {score2};")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            result=self.s2.execute(
                f"select faculties.name fac_name , subjects.name sub_name, AVG(score) from subjects inner join scores on subjects.id=id_subject inner join fac_dep on fac_dep.id=id_fac_dep inner join faculties on fac_dep.id_fac=faculties.id where faculties.name like '%{faculty}%' and subjects.name like '%{subject}%' group by faculties.name, subjects.name having AVG(score) between {score1} and {score2};")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_edu_price_less_faculty_department():", error)
        if not result:
            return "Can`t find"
        return result

    def find_student_subjects_on_fac_dep_semester(self,faculty,department,student,semester):
        result= None
        try:
            result=self.s.execute(
                f" select students.name stu_name,subjects.name sub_name from students inner join scores on scores.id_student=students.id inner join subjects on scores.id_subject=subjects.id inner join fac_dep on students.id_fac_dep=fac_dep.id inner join faculties on fac_dep.id_fac=faculties.id inner join departments on fac_dep.id_dep=departments.id where students.semester={semester} and subjects.semester={semester} and students.id_fac_dep=subjects.id_fac_dep and faculties.name = '{faculty}' and departments.name ='{department}' and students.name like '%{student}%';")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            result=self.s2.execute(
                f" select students.name stu_name,subjects.name sub_name from students inner join scores on scores.id_student=students.id inner join subjects on scores.id_subject=subjects.id inner join fac_dep on students.id_fac_dep=fac_dep.id inner join faculties on fac_dep.id_fac=faculties.id inner join departments on fac_dep.id_dep=departments.id where students.semester={semester} and subjects.semester={semester} and students.id_fac_dep=subjects.id_fac_dep and faculties.name = '{faculty}' and departments.name ='{department}' and students.name like '%{student}%';")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in find_student_subjects_on_fac_dep_semester():", error)
        if not result:
            return "Can`t find"
        return result

    def generate_fac_dep(self, number):
        try:
            self.s.execute(
                f"insert into fac_dep(id_fac,id_dep,price,name_head)select rnd.id_fac,rnd.id_dep, rnd.price, rnd.name_head from (select trunc(random()*(50000)+5000)::integer price, (md5(random()::text)||' '||md5(random()::text)) name_head, faculties.id id_fac, departments.id id_dep from   faculties, departments) rnd left join fac_dep on (rnd.id_fac=fac_dep.id_fac and rnd.id_dep=fac_dep.id_dep) where fac_dep.id is NULL order by random() LIMIT {number};")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.execute(
                f"insert into fac_dep(id_fac,id_dep,price,name_head)select rnd.id_fac,rnd.id_dep, rnd.price, rnd.name_head from (select trunc(random()*(50000)+5000)::integer price, (md5(random()::text)||' '||md5(random()::text)) name_head, faculties.id id_fac, departments.id id_dep from   faculties, departments) rnd left join fac_dep on (rnd.id_fac=fac_dep.id_fac and rnd.id_dep=fac_dep.id_dep) where fac_dep.id is NULL order by random() LIMIT {number};")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in generate_fac_dep():", error)
        return "Generated"

    def generate_score(self, number):
        try:
            self.s.execute(
                f"insert into scores(id_subject,id_student,score) select rnd.id_subject,rnd.id_student, rnd.score from (select trunc(random()*(100))::integer score, subjects.id id_subject,students.id id_student, subjects.semester sub_sem, students.semester stu_semester,subjects.id_fac_dep sub_fac_dep, students.id_fac_dep stu_fac_dep from   subjects, students) rnd left join scores on (rnd.id_subject=scores.id_subject and rnd.id_student=scores.id_student) where scores.id is NULL and rnd.sub_sem<rnd.stu_semester and rnd.sub_fac_dep=rnd.stu_fac_dep order by random() LIMIT {number};")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.execute(
                f"insert into scores(id_subject,id_student,score) select rnd.id_subject,rnd.id_student, rnd.score from (select trunc(random()*(100))::integer score, subjects.id id_subject,students.id id_student, subjects.semester sub_sem, students.semester stu_semester,subjects.id_fac_dep sub_fac_dep, students.id_fac_dep stu_fac_dep from   subjects, students) rnd left join scores on (rnd.id_subject=scores.id_subject and rnd.id_student=scores.id_student) where scores.id is NULL and rnd.sub_sem<rnd.stu_semester and rnd.sub_fac_dep=rnd.stu_fac_dep order by random() LIMIT {number};")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in generate_score():", error)
        return "Generated"

    def generate_subjects(self, number):
        try:
            self.s.execute(
                f"insert into subjects (name,semester,id_teacher,id_fac_dep) SELECT rnd.name,rnd.semester,rnd.id_teacher,rnd.id_fac_dep FROM (SELECT md5(random()::text) as name, trunc(random()*11+1) as semester, teachers.id as id_teacher, fac_dep.id as id_fac_dep FROM teachers,fac_dep )  as rnd ORDER BY random() LIMIT {number};")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.execute(
                f"insert into subjects (name,semester,id_teacher,id_fac_dep) SELECT rnd.name,rnd.semester,rnd.id_teacher,rnd.id_fac_dep FROM (SELECT md5(random()::text) as name, trunc(random()*11+1) as semester, teachers.id as id_teacher, fac_dep.id as id_fac_dep FROM teachers,fac_dep )  as rnd ORDER BY random() LIMIT {number};")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in generate_subjects():", error)
        return "Generated"

    def generate_students(self, number):
        try:
            self.s.execute(
                f"insert into students(name,date_of_birth,date_enter,phone,email,form_payment,id_fac_dep,semester,gender) SELECT name,date_of_birth,date_enter,phone,email,form_payment,id_fac_dep,semester,gender FROM (SELECT (md5(random()::text)||' '||(md5(random()::text))) as name, (timestamp'1980-01-01'+ random()*(timestamp'2000-01-01'- timestamp'1980-01-01')) as date_of_birth, (timestamp'2015-01-01'+ random()*(timestamp'2020-01-01'- timestamp'2015-01-01')) as date_enter,('+'||trunc(random()*8888888888+1111111111)) as phone, md5(random()::text) ||'@gmail.com' as email,(array['Budget','Contract'])[trunc(random()*2)+1] as form_payment, fac_dep.id as id_fac_dep,trunc(random()*11+1) as semester,(array['M','F'])[trunc(random()*2)+1] as gender FROM fac_dep, generate_series(1, 100) g) as rnd ORDER BY random() LIMIT {number};")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.execute(
                f"insert into students(name,date_of_birth,date_enter,phone,email,form_payment,id_fac_dep,semester,gender) SELECT name,date_of_birth,date_enter,phone,email,form_payment,id_fac_dep,semester,gender FROM (SELECT (md5(random()::text)||' '||(md5(random()::text))) as name, (timestamp'1980-01-01'+ random()*(timestamp'2000-01-01'- timestamp'1980-01-01')) as date_of_birth, (timestamp'2015-01-01'+ random()*(timestamp'2020-01-01'- timestamp'2015-01-01')) as date_enter,('+'||trunc(random()*8888888888+1111111111)) as phone, md5(random()::text) ||'@gmail.com' as email,(array['Budget','Contract'])[trunc(random()*2)+1] as form_payment, fac_dep.id as id_fac_dep,trunc(random()*11+1) as semester,(array['M','F'])[trunc(random()*2)+1] as gender FROM fac_dep, generate_series(1, 100) g) as rnd ORDER BY random() LIMIT {number};")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in generate_students():", error)
        return "Generated"

    def generate_teachers(self, number):
        try:
            self.s.execute(
                f"insert into teachers(name,date_of_birth,from_year,position,phone,email,gender) SELECT name,date_of_birth,from_year,position,phone,email,gender FROM (SELECT (md5(random()::text)||' '||(md5(random()::text))) as name, (timestamp'1980-01-01'+ random()*(timestamp'2000-01-01'- timestamp'1980-01-01')) as date_of_birth, trunc(random()*50+1950) as from_year,(array['Assistance','Head teacher','Docent','Professor'])[trunc(random()*4)+1] as position,('+'||trunc(random()*8888888888+1111111111)) as phone,md5(random()::text) ||'@gmail.com' as email,(array['M','F'])[trunc(random()*2)+1] as gender FROM generate_series(1, {number}) g) as rnd;")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.execute(
                f"insert into teachers(name,date_of_birth,from_year,position,phone,email,gender) SELECT name,date_of_birth,from_year,position,phone,email,gender FROM (SELECT (md5(random()::text)||' '||(md5(random()::text))) as name, (timestamp'1980-01-01'+ random()*(timestamp'2000-01-01'- timestamp'1980-01-01')) as date_of_birth, trunc(random()*50+1950) as from_year,(array['Assistance','Head teacher','Docent','Professor'])[trunc(random()*4)+1] as position,('+'||trunc(random()*8888888888+1111111111)) as phone,md5(random()::text) ||'@gmail.com' as email,(array['M','F'])[trunc(random()*2)+1] as gender FROM generate_series(1, {number}) g) as rnd;")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in generate_teachers():", error)
        return "Generated"

    def generate_faculties(self, number):
        try:
            self.s.execute(
                f"insert into faculties(name,name_dean,adress,phone,email,description)SELECT name,name_dean,adress,phone,email,description FROM (SELECT (md5(random()::text)) as name,(md5(random()::text)||' '||(md5(random()::text))) as name_dean, (md5(random()::text)) as adress,('+'||trunc(random()*8888888888+1111111111)) as phone,md5(random()::text) ||'@gmail.com' as email,(md5(random()::text)) as description FROM generate_series(1, {number}) g) as rnd;")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.execute(
                f"insert into faculties(name,name_dean,adress,phone,email,description)SELECT name,name_dean,adress,phone,email,description FROM (SELECT (md5(random()::text)) as name,(md5(random()::text)||' '||(md5(random()::text))) as name_dean, (md5(random()::text)) as adress,('+'||trunc(random()*8888888888+1111111111)) as phone,md5(random()::text) ||'@gmail.com' as email,(md5(random()::text)) as description FROM generate_series(1, {number}) g) as rnd;")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in generate_faculties():", error)
        return "Generated"

    def generate_departments(self, number):
        try:
            self.s.execute(
                f"insert into departments(name,study_form,description) SELECT name,study_form,description FROM (SELECT (md5(random()::text)) as name,(array['Daytime','Extramural'])[trunc(random()*2)+1] as study_form,(md5(random()::text)) as description FROM generate_series(1, {number}) g) as rnd;")
            self.s.commit()
        except exc.OperationalError:
            print("Go to slave server")
            self.s2.execute(
                f"insert into departments(name,study_form,description) SELECT name,study_form,description FROM (SELECT (md5(random()::text)) as name,(array['Daytime','Extramural'])[trunc(random()*2)+1] as study_form,(md5(random()::text)) as description FROM generate_series(1, {number}) g) as rnd;")
            self.s2.commit()
        except (Exception, exc.SQLAlchemyError) as error:
            self.s.rollback()
            self.s2.rollback()
            print("Error in generate_departments():", error)
        return "Generated"

    def filter_avg_price(self,study_form):
        try:
            df1= pd.read_sql_table('fac_dep', self._engine)
            df2 = pd.read_sql_table('departments', self._engine)
        except exc.OperationalError:
            print("Go to slave server")
            df1 = pd.read_sql_table('fac_dep', self._engine2)
            df2 = pd.read_sql_table('departments', self._engine2)
        df2=df2.rename(columns={'id':'id_dep'})
        df = pd.merge(df1,df2,how='inner',on='id_dep')
        df=df[df.study_form==study_form]
        new_df = df.groupby(['name'])['price'].mean()
        return new_df

    def find_student_subjects_scores(self,name):
        try:
            df1 = pd.read_sql_table('scores', self._engine)
            df2 = pd.read_sql_table('students', self._engine)
            df3 = pd.read_sql_table('subjects', self._engine)
        except exc.OperationalError:
            print("Go to slave server")
            df1 = pd.read_sql_table('scores', self._engine2)
            df2 = pd.read_sql_table('students', self._engine2)
            df3 = pd.read_sql_table('subjects', self._engine2)
        df2 = df2[df2.name == name]
        df2 = df2.rename(columns={'id': 'id_student','name':'student_name'})
        df3 = df3.rename(columns={'id': 'id_subject'})
        df = pd.merge(df1, df2, how='inner', on='id_student')
        df = pd.merge(df, df3, how='inner', on='id_subject')
        new_df = df.groupby(['name'])['score'].mean()
        return new_df

    def count_teacher_subjects(self,faculty):
        try:
            df1 = pd.read_sql_table('fac_dep', self._engine)
            df2 = pd.read_sql_table('faculties', self._engine)
            df3 = pd.read_sql_table('subjects', self._engine)
            df4 = pd.read_sql_table('teachers', self._engine)
        except exc.OperationalError:
            print("Go to slave server")
            df1 = pd.read_sql_table('fac_dep', self._engine2)
            df2 = pd.read_sql_table('faculties', self._engine2)
            df3 = pd.read_sql_table('subjects', self._engine2)
            df4 = pd.read_sql_table('teachers', self._engine2)
        df2 = df2[df2.name == faculty]
        df2 = df2.rename(columns={'id': 'id_fac', 'name': 'fac_name'})
        df = pd.merge(df1, df2, how='inner', on='id_fac')
        df3 = df3.rename(columns={ 'name': 'sub_name'})
        df4 = df4.rename(columns={'id': 'id_teacher'})
        df = df.rename(columns={'id': 'id_fac_dep'})
        df = pd.merge(df, df3, how='inner', on='id_fac_dep')
        df = pd.merge(df, df4, how='inner', on='id_teacher')
        new_df = df.groupby(['name'])['sub_name'].count()
        return new_df

    def count_teacher_position(self,faculty):
        try:
            df1 = pd.read_sql_table('fac_dep', self._engine)
            df2 = pd.read_sql_table('faculties', self._engine)
            df3 = pd.read_sql_table('subjects', self._engine)
            df4 = pd.read_sql_table('teachers', self._engine)
        except exc.OperationalError:
            df1 = pd.read_sql_table('fac_dep', self._engine2)
            df2 = pd.read_sql_table('faculties', self._engine2)
            df3 = pd.read_sql_table('subjects', self._engine2)
            df4 = pd.read_sql_table('teachers', self._engine2)
        df2 = df2[df2.name == faculty]
        df2 = df2.rename(columns={'id': 'id_fac', 'name': 'fac_name'})
        df = pd.merge(df1, df2, how='inner', on='id_fac')
        df3 = df3.rename(columns={ 'name': 'sub_name'})
        df4 = df4.rename(columns={'id': 'id_teacher'})
        df = df.rename(columns={'id': 'id_fac_dep'})
        df = pd.merge(df, df3, how='inner', on='id_fac_dep')
        df = pd.merge(df, df4, how='inner', on='id_teacher')
        new_df = df.groupby(['position'])['name'].count()
        return new_df




