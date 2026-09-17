import psycopg

try:
    # Подключение к базе данных PostgreSQL
    conn = psycopg.connect(
        host="localhost",
        dbname="tracks_db",
        user="postgres",
        password="Admin"
    )
    print("Успешное подключение к базе данных!")

    cur = conn.cursor()

    # === МЕНЯЙТЕ ТОЛЬКО ЭТОТ ЗАПРОС ДЛЯ КАЖДОГО ПУНКТА ===
    cur.execute('SELECT * FROM tracks WHERE "Длительность" > 200;')



    # ====================================================

    rows = cur.fetchall()
    if not rows:
        print("Запрос вернул пустой результат.")
    else:
        print(f"Найдено треков: {len(rows)}")
        for row in rows:
            print(row)

    cur.close()
    conn.close()
except Exception as e:
    # Убираем возможную ошибку кодировки в консоли Windows для кириллицы
    print(f"Ошибка при работе с БД: {e}")
