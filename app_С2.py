import psycopg2

# Настройки подключения к вашей базе данных
connection = psycopg2.connect(
    dbname="tracks_db", 
    user="postgres", 
    password="Admin", 
    host="localhost", 
    port="5432"
)

cursor = connection.cursor()
# СТРОКА 11: Запрос выводит только Название и Исполнителя
cursor.execute("SELECT Название, Исполнитель FROM tracks;") 

# Вывод результатов в консоль
rows = cursor.fetchall()
for row in rows:
    print(f"Название: {row[0]} | Исполнитель: {row[1]}")

cursor.close()
connection.close()
