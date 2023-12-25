import csv
import psycopg2

username = 'postgres'
password = 'Patniza13'
database = 'db_lab5'
host = 'localhost'
port = '5432'

try:
    conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
    cursor = conn.cursor()

    tables = ["Breweries", "Beer", "Beer_reviews"]

    for table in tables:
        csv_file_path = f"{table}.csv"

        with open(csv_file_path, 'w', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # Отримуємо ім'я стовпців з таблиці
            cursor.execute(f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table}'")
            columns = [column[0] for column in cursor.fetchall()]

            csv_writer.writerow(columns)

            # Отримуємо дані з таблиці та записуємо їх у CSV-файл
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            csv_writer.writerows(rows)

    print("Експорт даних в CSV успішно завершено.")

except psycopg2.Error as e:
    print(f"Помилка під час виконання SQL-запиту: {e}")

finally:
    # Завершення роботи з базою даних
    if conn is not None:
        conn.close()
