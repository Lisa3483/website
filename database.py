import sqlite3
import json
# Устанавливаем соединение с базой данных или создаем новую, если такой базы данных еще нет
conn = sqlite3.connect('mydatabase.db')

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Создаем таблицу с указанными столбцами
cursor.execute('''CREATE TABLE users
             (id INTEGER PRIMARY KEY,
             name TEXT NOT NULL,
             age INTEGER)''')

# Сохраняем изменения
conn.commit()

# Закрываем соединение
conn.close()