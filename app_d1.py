import psycopg

# 1. Подключение к базе данных
conn = psycopg.connect(
    host="localhost",
    dbname="tracks_db",  # Убедись, что имя БД совпадает с прошлыми шагами (tracks_db или tracks_bd)
    user="postgres",
    password="Admin"     # Твой пароль от pgAdmin
)
cur = conn.cursor()

# 2. Интерактивный ввод значений от пользователя
nazvanie = input("Название: ")
ispolnitel = input("Исполнитель: ")
god = int(input("Год: "))
dlitelnost = int(input("Длительность (сек): "))

# 3. Безопасный INSERT запрос через кортеж параметров (%s)
# Обязательно берем русские колонки в двойные кавычки
cur.execute(
    'INSERT INTO tracks ("Название", "Исполнитель", "Год", "Длительность") VALUES (%s, %s, %s, %s);',
    (nazvanie, ispolnitel, god, dlitelnost)
)

# ВАЖНО: Фиксируем транзакцию в БД, чтобы данные записались!
conn.commit()
print("Успешно добавлено в базу!")

# 4. Проверка: Вывод всех строк таблицы на экран
print("\nТекущее содержимое таблицы tracks:")
cur.execute('SELECT * FROM tracks;')
rows = cur.fetchall()
for row in rows:
    print(row)

# 5. Закрытие соединения
cur.close()
conn.close()
