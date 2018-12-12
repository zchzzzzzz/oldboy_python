import pymysql

conn1=pymysql.connect(host="127.0.0.1",db="zzz",port=3306,user="root",password="123456")
cursor=conn1.cursor(cursor=pymysql.cursors.DictCursor)
try:
 sql1="start transaction;"
 sql2="update account set balance=balance=-5000 where id=1;"
 sql3="update account set balance=balance=+5000 where id=2;"
 sql4="commit;"
 sql5="select * from account"

 cursor.execute(sql1)
 cursor.execute(sql2)
 raise Exception
 cursor.execute(sql3)
 cursor.close()
 conn1.commit()
except:
 conn1.rollback()
 conn1.commit()

cursor.execute(sql5)
result1=cursor.fetchall()
print(result1)
conn1.commit()
cursor.close()
conn1.close()
