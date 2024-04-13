import random
chances = [25, 20, 15, 35, 5]
total_chance = sum(chances)

random_number = random.uniform(0, total_chance)

current_chance = 0
for i, chance in enumerate(chances):
    current_chance += chance
    if random_number <= current_chance:
        print(f"Выбран элемент {i+1} с шансом {chance}%")
        break