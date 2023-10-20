import sqlite3
conn = sqlite3.connect("details.db")

st_name = input("Enter name:")
# data = conn.execute("SELECT * FROM student where st_name = " +st_name+ "")
data = conn.execute("SELECT * FROM student where st_name like '%3"+st_name+"%'|")

for i in data:
    print(i)