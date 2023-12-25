import psycopg2

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

    print("\nQuery 1: Number of Beer Types per Brewery\n")
    for row in cur:
        print(row)
        brewery_name.append(row[0])
        beer_types_count.append(row[1])

    print("\nPercentage Distribution:\n")
    for i in range(len(brewery_name)):
        print(f"{brewery_name[i]} {100*beer_types_count[i]/sum(beer_types_count):1.01f}%")

    # Запит 2
    cur.execute(query_2)
    country_of_origin = []
    beer_count = []

    print("\nQuery 2: Percentage Distribution of Beer Origin Countries\n")
    for row in cur:
        print(row)
        country_of_origin.append(row[0])
        beer_count.append(row[1])

    # Запит 3
    cur.execute(query_3)
    price = []
    average_rating = []

    print("\nQuery 3: Average Rating vs. Price for Beers\n")
    for row in cur:
        print(row)
        price.append(row[0])
        average_rating.append(row[1])
