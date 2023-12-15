import psycopg2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Змінні для підключення до бази даних
username = 'postgres'
password = 'Patniza13'
database = 'db_lab3'
host = 'localhost'
port = '5432'

# Запити для отримання даних з бази даних
queries = [
    '''
    SELECT b.brewery_name, COUNT(DISTINCT beer.type_of_beer) AS beer_types_count
    FROM Breweries b
    JOIN Beer ON b.id_brewery = beer.id_brewery
    GROUP BY b.brewery_name;
    ''',
    '''
    SELECT country_of_origin, COUNT(*) AS beer_count
    FROM Beer
    GROUP BY country_of_origin;
    ''',
    '''
    SELECT price, AVG(rating) AS average_rating
    FROM Beer_reviews br
    JOIN Beer b ON br.id_beer = b.id_beer
    GROUP BY price
    ORDER BY price;
    '''
]

# Запити для створення відображень в базі даних
create_views = [
    '''
    CREATE OR REPLACE VIEW brewery_beer_types AS
    SELECT b.brewery_name, COUNT(DISTINCT beer.type_of_beer) AS beer_types_count
    FROM Breweries b
    JOIN Beer ON b.id_brewery = beer.id_brewery
    GROUP BY b.brewery_name;
    ''',
    '''
    CREATE OR REPLACE VIEW beer_count_by_country AS
    SELECT country_of_origin, COUNT(*) AS beer_count
    FROM Beer
    GROUP BY country_of_origin;
    ''',
    '''
    CREATE OR REPLACE VIEW avg_rating_by_price AS
    SELECT price, AVG(rating) AS average_rating
    FROM Beer_reviews br
    JOIN Beer b ON br.id_beer = b.id_beer
    GROUP BY price
    ORDER BY price;
    '''
]

def execute_query_and_fetch_all(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

# Підключення до бази даних
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    # Виконання запитів для створення відображень в базі даних
    for create_view_query in create_views:
        cur.execute(create_view_query)

    # Виконання запитів для отримання даних з бази даних
    result_1 = execute_query_and_fetch_all(cur, queries[0])
    result_2 = execute_query_and_fetch_all(cur, queries[1])
    result_3 = execute_query_and_fetch_all(cur, queries[2])

def visualize_beer(result_1, result_2, result_3):
    # Отримання списку назв пивоварень та кількості видів пива для першого графіку
    brewery_names = [row[0] for row in result_1]
    beer_types_count = [row[1] for row in result_1]

    x_range = range(len(brewery_names))

    # Створення графіків
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3, figsize=(18, 6))
    
    # Гістограма для першого запиту (result_1)
    bar = bar_ax.bar(x_range, beer_types_count, label='Total')
    bar_ax.bar_label(bar, label_type='center', fmt='%d')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(brewery_names, rotation=90, ha='center')
    bar_ax.set_xlabel('Назви пивоварень')
    bar_ax.set_yticks(bar_ax.get_yticks())
    bar_ax.set_yticklabels(str(int(float(label))) for label in bar_ax.get_yticks())
    bar_ax.set_ylabel('Кількість видів пива')
    bar_ax.set_title('Кількість видів пива за пивоварнею')

    # Кругова діаграма для другого запиту (result_2)
    brewery_names_unique = [row[0] for row in result_2]
    beer_count = [row[1] for row in result_2]
    pie_ax.pie(beer_count, labels=brewery_names_unique, autopct='%1.01f%%')
    pie_ax.set_title('Розподіл пива за країнами походження')

    # Точкова діаграма для третього запиту (result_3)
    avg_rating = [round(row[0], 3) for row in result_3]
    count = [row[1] for row in result_3]
    graph_ax.plot(count, avg_rating, color='blue', marker='o')

    for cnt, rat, name in zip(count, avg_rating, brewery_names):
        graph_ax.annotate(name, xy=(cnt, rat), color='blue', textcoords='offset points')

    graph_ax.set_xlabel('Кількість видів пива')
    graph_ax.set_ylabel('Середній рейтинг')
    graph_ax.set_title('Залежність середнього рейтингу від кількості видів пива за пивоварнею')

    mng = plt.get_current_fig_manager()
    mng.resize(1800, 900)

    plt.show()

# Припускаючи, що запити визначені так, як раніше
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn.cursor() as cursor:
    # Виконання запитів до бази даних
    for query in queries:
        cursor.execute(query)

    # Виконання запитів для отримання даних з бази даних
    cursor.execute("SELECT * FROM brewery_beer_types")
    result_1 = cursor.fetchall()

    cursor.execute("SELECT * FROM beer_count_by_country")
    result_2 = cursor.fetchall()

    cursor.execute("SELECT * FROM avg_rating_by_price")
    result_3 = cursor.fetchall()

# Візуалізація отриманих даних
visualize_beer(result_1, result_2, result_3)
