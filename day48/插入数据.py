import pymysql

conn1 = pymysql.connect(host="127.0.0.1", db="zzz", port=3306, user="root", password="123456")
cursor = conn1.cursor(cursor=pymysql.cursors.DictCursor)
sql1 = "start transaction;"
sql2 = "select * from z20181128"
sql3="""insert into z20181128(id,name) values(2,"abc")"""

try:
 cursor.execute(sql1)
 cursor.execute(sql2)
 conn1.commit()
 raise Exception
 cursor.execute(sql3)
 cursor.close()
 conn1.commit()
except Exception as e:
   conn1.rollback()
   conn1.commit()
result1 = cursor.fetchall()

print(result1)
conn1.commit()
cursor.close()
conn1.close()
