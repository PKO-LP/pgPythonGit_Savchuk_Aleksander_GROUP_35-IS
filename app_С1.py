import psycopg

try:
    # Подключение к базе данных PostgreSQL
    conn = psycopg.connect(
        host="localhost",
        dbname="tracks_db",
        user="postgres",
        password="Admin"  # <-- Убедитесь, что тут правильный пароль от вашего pgAdmin
    )
    print("Успешное подключение к базе данных!")

    # Создание курсора
    cur = conn.cursor()

    # Выполнение запроса
    cur.execute('SELECT "Название", "Исполнитель", "Год", "Длительность" FROM tracks;')
    rows = cur.fetchall()

    if not rows:
        print("Подключение есть, но таблица 'tracks' пустая. Добавьте данные через pgAdmin!")
    else:
        print(f"Найдено треков: {len(rows)}")
        for row in rows:
            print(row)

    # Закрытие соединения
    cur.close()
    conn.close()

except Exception as e:
    print(f"Ошибка при работе с БД: {e}")
