import sqlite3
conn = sqlite3.connect("details.db")

conn.execute("""
             update student set st_name = 'Ram Gautam' where st_id = 1
             """)
conn.commit()
conn.close()