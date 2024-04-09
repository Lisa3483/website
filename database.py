import sqlite3
import json
conn = sqlite3.connect('cases_info.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE cases
             (id INTEGER PRIMARY KEY)''')
conn.commit()
conn.close()
