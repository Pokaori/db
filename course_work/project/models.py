from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, ForeignKey, Table, Date, CHAR, UniqueConstraint
from sqlalchemy.orm import relationship, backref


Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date_of_birth = Column(Date)
    date_enter = Column(Date)
    phone = Column(Text)
    email = Column(Text)
    form_payment = Column(Text)
    semester = Column(Integer)
    gender = Column(CHAR)
    id_fac_dep = Column(Integer, ForeignKey('fac_dep.id'))
    scores = relationship("Score", cascade="all, delete", backref="students")

    def __repr__(self):
        return "<Student (id={}, name='{}', date_of_birth='{}', date_enter ='{}', phone='{}', email='{}',form_payment='{}', semester ='{}', gender='{}', id_fac_dep='{}' )>" \
            .format(self.id, self.name, self.date_of_birth, self.date_enter, self.phone, self.email,self.form_payment, self.semester, self.gender, self.id_fac_dep)


class Teacher(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    date_of_birth = Column(Date)
    from_year = Column(Integer)
    position = Column (Text)
    phone = Column(Text)
    email = Column(Text)
    gender = Column(CHAR)
    subjects = relationship("Subject", cascade="all, delete", backref="teachers")

    def __repr__(self):
        return "<Teacher(id={}, name='{}', date_of_birth='{}', from_year='{}', position='{}', phone='{}', email='{}', gender='{}')>" \
            .format(self.id, self.name, self.date_of_birth, self.from_year, self.position, self.phone, self.email, self.gender)

class Department(Base):
    __tablename__ = 'departments'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    study_form = Column(Text)
    description = Column(Text)
    fac_dep=relationship("Fac_dep", cascade="all, delete", backref="departments")
    def __repr__(self):
        return "<Department(id={}, name='{}', study_form='{}', description='{}')>" \
            .format(self.id, self.name, self.study_form, self.description)

class Faculty(Base):
    __tablename__ = 'faculties'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    name_dean = Column(Text)
    adress = Column(Text)
    phone = Column(Text)
    email = Column(Text)
    description = Column(Text)
    def __repr__(self):
        return "<Faculty(id={}, name='{}', name_dean='{}', adress='{}', phone='{}', email='{}',desdription='{}' )>" \
            .format(self.id, self.name, self.name_dean, self.adress, self.phone, self.email ,self.desdription)

class Fac_dep(Base):
    __tablename__ = 'fac_dep'
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    id_fac =  Column(Integer, ForeignKey('faculties.id'))
    id_dep = Column(Integer, ForeignKey('departments.id'))
    name_head = Column (Text)
    subjects = relationship("Subject", cascade="all, delete", backref="fac_dep")
    def __repr__(self):
        return "<Fac_dep(id={}, price='{}', id_fac='{}', id_dep='{}', name_head='{}')>" \
            .format(self.id, self.price, self.id_fac, self.id_dep, self.name_head)

class Score(Base):
    __tablename__ = 'scores'
    id = Column(Integer, primary_key=True)
    score = Column(Integer)
    id_subject = Column(Integer, ForeignKey('subjects.id'))
    id_student = Column(Integer, ForeignKey('students.id'))


    def __repr__(self):
        return "<Score(id={}, score='{}', id_subject='{}', id_student='{}')>" \
            .format(self.id, self.score, self.id_subject, self.id_student)

class Subject(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    semester = Column(Integer)
    id_teacher = Column(Integer, ForeignKey('teachers.id'))
    id_fac_dep = Column(Integer, ForeignKey('fac_dep.id'))
    scores = relationship("Score", cascade="all, delete", backref="subjects")
    def __repr__(self):
        return "<Subject(id={}, name='{}', semester='{}', id_teacher='{}', id_fac_dep='{}')>" \
            .format(self.id, self.name, self.semester, self.id_teacher,self.id_fac_dep)



