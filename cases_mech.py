import json
import random
import sqlite3

import requests


class Cases_mechanic:
    def __init__(self):
        pass

    def get_reqests(self):
        pass

    def get_win(self, table_name):
        id_of_img = 1
        conn = sqlite3.connect('cases_info.db')
        cursor = conn.cursor()
        cursor.execute(f'''SELECT chance FROM {table_name}''')
        chances = cursor.fetchall()

        total_chance = sum(chances)

        random_number = random.uniform(0, total_chance)

        current_chance = 0
        for i, chance in enumerate(chances):
            current_chance += chance
            if random_number <= current_chance:
                id_of_img = i
                break
        cursor.execute(f'''SELECT img_name, cost FROM {table_name} WHERE id = {str(id_of_img)}''')
        img_name, cost = cursor.fetchall()
        conn.commit()
        conn.close()
        json.dump(img_name, cost)

    def sell(self):
        conn = sqlite3.connect('../files/files_db/cases_info.db')
        cursor = conn.cursor()

