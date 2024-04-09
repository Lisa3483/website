import sqlite3
import json
conn = sqlite3.connect('cases_info.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Table_hedgehogs
                (id INTEGER PRIMARY KEY,
                chance REAL,
                cost REAL,
                img_name TEXT)''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Table_cats
                (id INTEGER PRIMARY KEY,
                chance REAL,
                cost REAL,
                img_name TEXT)''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Table_dogs
                (id INTEGER PRIMARY KEY,
                chance REAL,
                cost REAL,
                img_name TEXT)''')

conn.commit()
conn.close()
