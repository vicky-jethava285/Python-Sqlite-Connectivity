import sqlite3

con=sqlite3.connect('Student.db')
cur=con.cursor()
cur.execute("""delete from student where id=1""")
print("Delete data successfully..!")