import psycopg2
from sqlalchemy import create_engine, exc
from sqlalchemy.orm import sessionmaker
import csv
from faker import Faker
import datetime
import random



DATABASE_URI = 'postgres+psycopg2://postgres:16072002p@localhost:5432/Course_work'
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
s = Session()
fake=Faker()
# with open('data/TX.TXT') as csv_file:
#     csv_reader=csv.reader(csv_file,delimiter=',')
#     for row in csv_reader:
#         start_date=datetime.date(1950,1,1)
#         end_date=datetime.date(2000,1,1)
#         time_between_dates=end_date-start_date
#         between_dates=time_between_dates.days
#         random_number_of_days=random.randrange(between_dates)
#         random_date=start_date+datetime.timedelta(days=random_number_of_days)
#         start_date2=datetime.date(random_date.year+20,1,1)
#         end_data2=datetime.date(2020,1,1)
#         time_between_dates2 = end_data2 - start_date2
#         between_dates2 = time_between_dates.days
#         random_number_of_days2 = random.randrange(between_dates2)
#         random_date2 = start_date2 + datetime.timedelta(days=random_number_of_days2)
#         positions=["Assistance","Head teacher","Docent","Professor"]
#         rand_pos=random.choice(positions)
#         phone=random.randrange(111111111,999999999)
#         s.execute(F"Insert into teachers (name,date_of_birth,from_year,position,phone,email,gender) VALUES ('{row[3]+' '+fake.last_name()}','{random_date}',{random_date2.year},'{rand_pos}','{'+'+str(phone)}','{fake.email()}','{row[1]}')")
#         s.commit()

# with open('data/Department_Information.csv') as csv_file:
#     csv_reader=csv.reader(csv_file,delimiter=',')
#     for row in csv_reader:
#         s.execute(F"Insert into departments (name,study_form,description) VALUES ('{row[1]}','Daytime','{fake.text()}')")
#         s.commit()
#         s.execute(F"Insert into departments (name,study_form,description) VALUES ('{row[1]}','Extramural','{fake.text()}')")
#         s.commit()

# with open('data/CA.csv') as csv_file:
#     csv_reader=csv.reader(csv_file,delimiter=',')
#     for row in csv_reader:
#         start_date=datetime.date(1990,1,1)
#         end_date=datetime.date(2004,1,1)
#         time_between_dates=end_date-start_date
#         between_dates=time_between_dates.days
#         random_number_of_days=random.randrange(0,between_dates)
#         random_date=start_date+datetime.timedelta(days=random_number_of_days)
#         start_date2=datetime.date(random_date.year+15,1,1)
#         end_data2=datetime.date(2020,1,1)
#         time_between_dates2 = end_data2 - start_date2
#         between_dates2 = time_between_dates2.days
#         random_number_of_days2 = random.randrange(0,between_dates2)
#         random_date2 = start_date2 + datetime.timedelta(days=random_number_of_days2)
#         print(random_date.year)
#         print(random_date2.year)
#         print(' ')
#         semester=random.randrange(1,min(12,((2020-random_date2.year+1)*2)))
#         form_payments=["Budget","Contract"]
#         rand_pay=random.choice(form_payments)
#         phone=random.randrange(111111111,999999999)
#         id_fac_dep = random.randrange(1, 64)
#         s.execute(F"Insert into students(name,date_of_birth,date_enter,phone,email,form_payment,id_fac_dep,semester,gender) VALUES ('{row[3]+' '+fake.last_name()}','{random_date}','{random_date2}','{'+'+str(phone)}','{fake.email()}','{rand_pay}','{id_fac_dep}',{semester},'{row[1]}')")
#         s.commit()
with open('../subjects/subjects.csv') as csv_file:
    csv_reader=csv.reader(csv_file,delimiter=',')
    n=0
    for row in csv_reader:
        if n%2==0:
            semester = random.randrange(1, 12)
            id_teacher= random.randrange(10150, 10500)
            id_fac_dep = random.randrange(1,64)
            s.execute(F"Insert into subjects (name,semester,id_teacher,id_fac_dep) VALUES ($${row[0]}$$,{semester},{id_teacher},{id_fac_dep})")
            s.commit()
        n=n+1


s.close()
