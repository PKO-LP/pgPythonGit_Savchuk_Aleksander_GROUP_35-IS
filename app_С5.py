import psycopg

try:
    conn = psycopg.connect(
        host="localhost",
        dbname="tracks_db",
        user="postgres",
        password="Admin"
    )
    print("Успешное подключение к базе данных!")

    cur = conn.cursor()

    # Запрос выводит только "Название" и "Год" для треков новее 2015 года
    cur.execute('SELECT "Название", "Год" FROM tracks WHERE "Год" > 2015;')

    rows = cur.fetchall()
    if not rows:
        print("Треки после 2015 года не найдены.")
    else:
        print(f"Найдено треков: {len(rows)}")
        for row in rows:
            print(row)

    cur.close()
    conn.close()
except Exception as e:
    print(f"Ошибка при работе с БД: {e}")
