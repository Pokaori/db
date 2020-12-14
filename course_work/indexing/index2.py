import psycopg2
import matplotlib.pyplot as plt
connect =psycopg2.connect(user="postgres", password="16072002p", host="localhost", port="5432", database="Course_work")
cursor =connect.cursor()
cursor.execute("explain analyze select score from scores where score<40 and score>80")
connect.commit()
res=cursor.fetchall()
# res=(x for x in res if (x.find('Execution')>-1))
results=[]
cursor.execute('set enable_seqscan to on;')
connect.commit()
for j in range(100):
    cursor.execute("explain analyze select name from students where name ='Mary Knox'")
    connect.commit()
    res = cursor.fetchall()
    for i in res:
        if(i[0].find('Execution')>-1):
            result=None
            for j in i[0].split():
                try:
                    result = float(j)
                    break
                except:
                    continue
            results.append(result)
cursor.execute('create index ind2 on students(name);')
connect.commit()
cursor.execute('set enable_seqscan to off;')
connect.commit()
results2=[]
for j in range(100):
    cursor.execute("explain analyze select name from students where name ='Mary Knox'")
    connect.commit()
    res = cursor.fetchall()
    for i in res:
        if(i[0].find('Execution')>-1):
            result=None
            for j in i[0].split():
                try:
                    result = float(j)
                    break
                except:
                    continue
            results2.append(result)
print(results)
print(results2)
plt.plot(results)
plt.plot(results2)
plt.show()
cursor.close()
connect.close()