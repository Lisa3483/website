import sqlite3

conn = sqlite3.connect('cases_info.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Table_hedgehogs
                (id INTEGER PRIMARY KEY,
                chance REAL,
                cost REAL,
                img_name TEXT)''')
cursor.execute('''INSERT INTO Table_hedgehogs (chance, cost, img_name) VALUES (0.05, 10000, 'hedgehog1.png');
INSERT INTO Table_hedgehogs (chance, cost, img_name) VALUES (0.1, 20000, 'hedgehog2.png');
INSERT INTO Table_hedgehogs (chance, cost, img_name) VALUES (0.15, 30000, 'hedgehog3.png');
INSERT INTO Table_hedgehogs (chance, cost, img_name) VALUES (0.2, 40000, 'hedgehog4.png');
INSERT INTO Table_hedgehogs (chance, cost, img_name) VALUES (0.25, 50000, 'hedgehog5.png')''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Table_cats
                (id INTEGER PRIMARY KEY,
                chance REAL,
                cost REAL,
                img_name TEXT)''')
cursor.execute('''INSERT INTO Table_cats (chance, cost, img_name) VALUES (0.05, 10000, 'hedgehog1.png');
INSERT INTO Table_cats (chance, cost, img_name) VALUES (0.1, 20000, 'hedgehog2.png');
INSERT INTO Table_cats (chance, cost, img_name) VALUES (0.15, 30000, 'hedgehog3.png');
INSERT INTO Table_cats (chance, cost, img_name) VALUES (0.2, 40000, 'hedgehog4.png');
INSERT INTO Table_cats (chance, cost, img_name) VALUES (0.25, 50000, 'hedgehog5.png')''')
cursor.execute('''CREATE TABLE IF NOT EXISTS Table_dogs
                (id INTEGER PRIMARY KEY,
                chance REAL,
                cost REAL,
                img_name TEXT)''')
cursor.execute('''INSERT INTO Table_dogs (chance, cost, img_name) VALUES (0.05, 10000, 'hedgehog1.png');
INSERT INTO Table_dogs (chance, cost, img_name) VALUES (0.1, 20000, 'hedgehog2.png');
INSERT INTO Table_dogs (chance, cost, img_name) VALUES (0.15, 30000, 'hedgehog3.png');
INSERT INTO Table_dogs (chance, cost, img_name) VALUES (0.2, 40000, 'hedgehog4.png');
INSERT INTO Table_dogs (chance, cost, img_name) VALUES (0.25, 50000, 'hedgehog5.png')''')
conn.commit()
conn.close()
