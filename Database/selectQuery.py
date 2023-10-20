import sqlite3
conn = sqlite3.connect("details.db")

data = conn.execute("SELECT * FROM Student")

# limit--------->keyword

# data = conn.execute("SELECT * FROM Student limit 2,5")
# print("STUDENT ID","STUDENT NAME")
for i in data:
    print(i)
    # print(i[0],i[1])
    
    
    
    
