import sqlite3
conn = sqlite3.connect("details.db")

# conn.execute('''
#              Create table Student(
#                 st_id INT AUTO_INCREMENT PRIMARY KEY,
#                 st_name VARCHAR(50),
#                 st_class VARCHAR(10),
#                 st_email VARCHAR(30)
#              )
#              ''')

conn.execute('''
             Create table Fees(
                st_id INT AUTO_INCREMENT PRIMARY KEY,
                st_fee INT,
                st_class VARCHAR(10),
                st_email VARCHAR(30)
             )
             ''')
conn.close()