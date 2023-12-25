--1. Знайти середній рейтинг для пива від пивоварень, які були засновані до 2010 року:
select breweries.brewery_name, avg(beer_reviews.rating) as average_rating from breweries
inner join beer on breweries.id_brewery = beer.id_brewery
inner join beer_reviews on beer.id_beer = beer_reviews.id_beer
where breweries.year_of_establishment <= '2010-12-31'
group by breweries.brewery_name;


--2. Знайти обзори, в яких рейтинг більше 4 та коментар складається з більше ніж 20 символів:
SELECT 
    B.id_beer,
    B.beer_name,
    B.type_of_beer,
    B.alcohol_content,
    B.country_of_origin,
    B.price,
    COUNT(R.id_review) AS total_reviews
FROM 
    Beer B
LEFT JOIN 
    Beer_reviews R ON B.id_beer = R.id_beer
WHERE 
    R.rating > 4
GROUP BY 
    B.id_beer;


--3. Знайти пиво з найвищим рейтингом і його пивоварню:
select beer.beer_name, beer.type_of_beer, beer.alcohol_content, beer.price
from beer_reviews
inner join (
  select id_beer, max(rating) as max_rating
  from beer_reviews
  group by id_beer
) as MaxRatings
on beer_reviews.id_beer = MaxRatings.id_beer and beer_reviews.rating = MaxRatings.max_rating
inner join beer on beer_reviews.id_beer = beer.id_beer
inner join breweries on beer.id_brewery = breweries.id_brewery;
