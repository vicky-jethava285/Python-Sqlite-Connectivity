import sqlite3

con=sqlite3.connect('Student.db')
cur=con.cursor()
cur.execute("""update student set age=21 where name="vikas" """)
print("Update data successfully..!")