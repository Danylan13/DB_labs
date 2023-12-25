import psycopg2
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Змінні для підключення до бази даних
username = 'postgres'
password = 'Patniza13'
database = 'db_lab4'
host = 'localhost'
port = '5432'

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
    CREATE OR REPLACE VIEW alcohol_content_vs_review_count AS
    SELECT b.alcohol_content, COUNT(br.id_review) AS review_count
    FROM Beer b
    LEFT JOIN Beer_reviews br ON b.id_beer = br.id_beer
    GROUP BY b.alcohol_content
    ORDER BY b.alcohol_content;
    '''
]

# Підключення до бази даних
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

def visualize_beer(result_1, result_2, result_3):
    # Отримання списку назв пивоварень та кількості видів пива для першого графіку
    brewery_name = []
    beer_types_count = []

    for row in result_1:
        brewery_name.append(row[0])
        beer_types_count.append(row[1])


    x_range = range(len(brewery_name))

    # Створення графіків
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3, figsize=(18, 6))
    
    # Гістограма для першого запиту (result_1)
    bar = bar_ax.bar(x_range, beer_types_count, label='Total')
    bar_ax.bar_label(bar, label_type='center', fmt='%d')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(brewery_name, rotation=90, ha='center')
    bar_ax.set_xlabel('Brewery Names')
    bar_ax.set_yticks(bar_ax.get_yticks())
    bar_ax.set_yticklabels(str(int(float(label))) for label in bar_ax.get_yticks())
    bar_ax.set_ylabel('Count')
    bar_ax.set_title('Number of Beer Types per Brewery')

    # Кругова діаграма для другого запиту (result_2)
    brewery_names_unique = [row[0] for row in result_2]
    beer_count = [row[1] for row in result_2]
    pie_ax.pie(beer_count, labels=brewery_names_unique, autopct='%1.01f%%')
    pie_ax.set_title('Percentage Distribution of Beer Origin Countries')

    # Точкова діаграма для третього запиту (result_3)
    alcohol_content = []
    review_count = []

    for row in result_3:
        alcohol_content.append(row[0])
        review_count.append(row[1])

    graph_ax.plot(alcohol_content, review_count, color='green', marker='o')

    for alc, count in zip(alcohol_content, review_count):
        graph_ax.annotate(count, xy=(alc, count), color='green', textcoords='offset points')

    graph_ax.set_xlabel('Alcohol Content')
    graph_ax.set_ylabel('Review Count')
    graph_ax.set_title('Review Count vs. Alcohol Content for Beers')



    mng = plt.get_current_fig_manager()
    mng.resize(1800, 900)

    plt.show()

# Припускаючи, що запити визначені так, як раніше
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn.cursor() as cursor:
    # Виконання запитів до бази даних
    for query in create_views:
        cursor.execute(query)

    # Виконання запитів для отримання даних з бази даних
    cursor.execute("SELECT * FROM brewery_beer_types")
    result_1 = cursor.fetchall()

    cursor.execute("SELECT * FROM beer_count_by_country")
    result_2 = cursor.fetchall()

    cursor.execute("SELECT * FROM alcohol_content_vs_review_count")
    result_3 = cursor.fetchall()

    # Візуалізація отриманих даних
    visualize_beer(result_1, result_2, result_3)
