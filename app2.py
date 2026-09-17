import psycopg2

# Настройки подключения к вашей базе данных
connection = psycopg2.connect(
    dbname="your_db_name", 
    user="postgres", 
    password="your_password", 
    host="localhost", 
    port="5432"
)

cursor = connection.cursor()
# СТРОКА 11: Запрос выводит только Название и Исполнителя
cursor.execute("SELECT title, artist FROM tracks;") 

# Вывод результатов в консоль
rows = cursor.fetchall()
for row in rows:
    print(f"Название: {row[0]} | Исполнитель: {row[1]}")

cursor.close()
connection.close()
