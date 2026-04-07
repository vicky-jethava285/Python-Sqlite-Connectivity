import sqlite3

# connect to database (creates it if not exists)
conn = sqlite3.connect("Student.db")

# create cursor
cur = conn.cursor()

# select all records
cur.execute("SELECT * FROM student")

# fetch all rows
rows = cur.fetchall()

for row in rows:
    print(row)

# close connection
conn.close()

# 2. SELECT specific columns (don’t overfetch)

# cur.execute("SELECT name, email FROM users")
# rows = cur.fetchall()

# for name, email in rows:
#     print(name, email)