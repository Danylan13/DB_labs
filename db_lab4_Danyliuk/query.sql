--1. (Запит для стовпчикової діаграми) Візуалізація кількості видів пива (type_of_beer) у кожному пивоварні (brewery_name).
SELECT b.brewery_name, COUNT(DISTINCT beer.type_of_beer) AS beer_types_count
FROM Breweries b
JOIN Beer ON b.id_brewery = beer.id_brewery
GROUP BY b.brewery_name;

--2. (Запит для кругової діаграми) Візуалізація відсоткового співвідношення країн походження пива.
SELECT country_of_origin, COUNT(*) AS beer_count
FROM Beer
GROUP BY country_of_origin;

--3. (Запит для графіка залежності) Візуалізація середнього рейтингу (rating) пива від його вартості (price).
SELECT price, AVG(rating) AS average_rating
FROM Beer_reviews br
JOIN Beer b ON br.id_beer = b.id_beer
GROUP BY price
ORDER BY price;
