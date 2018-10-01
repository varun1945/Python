import sqlite3
db=sqlite3.connect('student1.db')
c=db.cursor()
c.execute("insert into data4 values('vinit',61,'vinit2gmail.com')")
c.execute("insert into data4 values('yash',64,'yash@gmail.com')")
c.execute("delete from data4 where roll=64")
c.execute("insert into data4 values('xyz',100,'xyz@gmail.com')")
c.execute("select * from data4")
"""r=c.fetchall()
for i in r:
    print(i)"""
#c.execute("update  data4 set name='qwerty' where roll =45")
data=c.execute("select name,roll from data4 where roll=45")
for i in data:
    print(i[0]," ",i[1])


db.commit()
c.close()
db.close()
