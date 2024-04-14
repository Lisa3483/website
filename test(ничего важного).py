import requests
def main():
    url = "http://127.0.0.1:5000"  # Замените на URL вашего JSON-файла
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на ошибки HTTP
        json_data = response.json()  # Преобразование ответа в JSON формат
        print(json_data)  # Вывод JSON-данных
    except requests.exceptions.RequestException as e:
        print("Ошибка при выполнении запроса:", e)

if __name__ == "__main__":
    while True:
        main()
