import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = 'Patniza13'
database = 'db_lab4'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT b.brewery_name, COUNT(DISTINCT beer.type_of_beer) AS beer_types_count
FROM Breweries b
JOIN Beer ON b.id_brewery = beer.id_brewery
GROUP BY b.brewery_name;
'''

query_2 = '''
SELECT country_of_origin, COUNT(*) AS beer_count
FROM Beer
GROUP BY country_of_origin;
'''

query_3 = '''
SELECT price, AVG(rating) AS average_rating
FROM Beer_reviews br
JOIN Beer b ON br.id_beer = b.id_beer
GROUP BY price
ORDER BY price;
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()

    # Запит 1
    cur.execute(query_1)
    brewery_name = []
    beer_types_count = []

    for row in cur:
        brewery_name.append(row[0])
        beer_types_count.append(row[1])

    x_range = range(len(brewery_name))

    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, beer_types_count, label='Beer Types Count')
    bar_ax.bar_label(bar, label_type='center', fmt='%d')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(brewery_name, rotation=90)
    bar_ax.set_xlabel('Brewery Names')
    bar_ax.set_yticks(bar_ax.get_yticks())
    bar_ax.set_yticklabels(str(int(float(label))) for label in bar_ax.get_yticks())
    bar_ax.set_ylabel('Count')
    bar_ax.set_title('Number of Beer Types per Brewery')

    # Запит 2
    cur.execute(query_2)
    country_of_origin = []
    beer_count = []

    for row in cur:
        country_of_origin.append(row[0])
        beer_count.append(row[1])

    pie_ax.pie(beer_count, labels=country_of_origin, autopct='%1.01f%%')
    pie_ax.set_title('Percentage Distribution of Beer Origin Countries')

    # Запит 3
    cur.execute(query_3)
    price = []
    average_rating = []

    for row in cur:
        price.append(row[0])
        average_rating.append(row[1])

    graph_ax.plot(price, average_rating, color='blue', marker='o')

    for p, r in zip(price, average_rating):
        graph_ax.annotate(r, xy=(p, r), color='blue', textcoords='offset points')

    graph_ax.set_xlabel('Price')
    graph_ax.set_ylabel('Average Rating')
    graph_ax.set_title('Average Rating vs. Price for Beers')

mng = plt.get_current_fig_manager()
mng.resize(1700, 900)

plt.show()
