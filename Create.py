import sqlite3

con=sqlite3.connect('Student.db')
cur=con.cursor()
cur.execute("""create table student(id integer,name text not null,age integer check(age>20),email text unique)""")
con.commit()
