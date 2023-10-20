import sqlite3
conn = sqlite3.connect("details.db")

ins = '''

insert into student (st_name, st_class,st_email) VALUES ('Ravi1','11th','sams00@gmail.com')
'''
conn.execute(ins)
conn.commit()
conn.close()