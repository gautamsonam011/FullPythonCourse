import sqlite3
conn = sqlite3.connect("details.db")

print("STUDENT ID","STUDENT NAME","STUDENT FEES")
data = conn.execute("SELECT f.st_id, s.st_name,f.fees FROM fees as f inner join student as s on f.st_id = s.st_id")

for i in data:
    print(i)
    
conn.close()
