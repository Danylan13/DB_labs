import csv
import psycopg2

# Креденціали PostgreSQL
username = 'postgres'
password = 'Patniza13'
database = 'db_lab5'
host = 'localhost'
port = '5432'

# Шлях до CSV-файлу для даних про пиво
csv_file_path = "beers.csv"

# З'єднання з базою даних PostgreSQL
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

# Створення курсора
cur = conn.cursor()

# Очистка існуючих даних з таблиць
clear_query = '''
DELETE FROM Beer_reviews;
DELETE FROM Beer;
DELETE FROM Breweries;
'''
cur.execute(clear_query)

# Відкриття CSV-файлу та імпорт даних в кожну таблицю
with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for row in csv_reader:
        # Видобування даних з рядка
        id_beer, beer_name, type_of_beer, alcohol_content, country_of_origin, price, id_brewery = row

        # Вставка даних в таблицю Breweries
        cur.execute("INSERT INTO Breweries (id_brewery, brewery_name, Location, year_of_establishment) VALUES (%s, %s, %s, %s) ON CONFLICT (id_brewery) DO NOTHING",
                    (id_brewery, 'Назва пивоварні', 'Місце розташування', '1900-01-01'))

        # Вставка даних в таблицю Beer
        cur.execute("INSERT INTO Beer (id_beer, beer_name, type_of_beer, alcohol_content, country_of_origin, price, id_brewery) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (id_beer) DO NOTHING",
                    (id_beer, beer_name, type_of_beer, float(alcohol_content), country_of_origin, float(price), id_brewery))

        # Вставка даних в таблицю Beer_reviews (Можливо, доведеться налаштувати цю частину залежно від структури вашого набору даних)
        cur.execute("INSERT INTO Beer_reviews (id_review, review_date, author, rating, comment, id_beer) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (id_review) DO NOTHING",
                    (id_beer, '1900-01-01', 'Ім\'я автора', 5.0, 'Коментар', id_beer))

# Збереження змін та закриття курсора та з'єднання
conn.commit()
cur.close()
conn.close()
