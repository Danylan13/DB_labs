import csv
import psycopg2
from datetime import datetime

username = 'postgres'
password = 'an.21092004'
database = 'danya'
host = 'localhost'
port = '5432'

csv_file1_path = "brewery.csv"
csv_file2_path = "beers.csv"
csv_file3_path = "reviews.csv"

finish_brewery = -1
finish_beer = -1
finish_reviews = 30000

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

cur = conn.cursor()

clear_query ='''
             DELETE FROM Beer_reviews;
             DELETE FROM Beer;
             DELETE FROM Breweries;
             '''
cur.execute(clear_query)

# First file
with open(csv_file1_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    count_breweries = 0
    for row in csv_reader:
        count_breweries += 1
        id_brewery, brewery_name, city, state, country, notes, types = row
        location = city + ", " + country

        cur.execute("INSERT INTO Breweries (id_brewery, brewery_name, Location, year_of_establishment) VALUES (%s, %s, %s, %s) returning id_brewery",
                    (id_brewery, brewery_name, location, datetime.now().date()))
        if count_breweries == finish_beer:
            break

# Second file
with open(csv_file2_path, 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    count_beer = 0
    for row in csv_reader:
        count_beer += 1
        id_beer, beer_name, id_brewery, state, country_of_origin, type_of_beer, availability, alcohol_content, notes, retired = row
        if alcohol_content == "":
            alcohol_content = -1

        cur.execute("INSERT INTO Beer (id_beer, beer_name, type_of_beer, alcohol_content, country_of_origin, price, id_brewery) VALUES (%s, %s, %s, %s, %s, %s, %s) returning id_beer",
                    (id_beer, beer_name, type_of_beer, alcohol_content, country_of_origin, alcohol_content, id_brewery))
        if count_beer == finish_beer:
            break

## Third file
#id_review = 0
#with open(csv_file3_path, 'r', encoding='utf-8') as csv_file:
#    csv_reader = csv.reader(csv_file)
#    next(csv_reader)
#    for row in csv_reader:
#        id_beer, author, review_date, comment, look, smell, taste, feel, overall, rating = row
#
#        if id_review <= finish_reviews:
#            try:
#                cur.execute("INSERT INTO Beer_reviews (id_review, review_date, author, rating, comment, id_beer) VALUES (%s, %s, %s, %s, %s, %s)",
#                            (id_review, review_date, author, rating, comment, id_beer))
#                id_review += 1
#            except:
#                id_review += 1
#                continue
#        else:
#            break

conn.commit()
cur.close()
conn.close()
