import sqlite3
con=sqlite3.connect('Student.db')
cur=con.cursor()
query=("""insert into student(id,name,age,email)values(1,"vikas",21,"vikas@gmail.com")""")
cur.execute(query)
print("DATA SUCCESSFULLY ADD....!")
