-- Виклик функції
SELECT avg_beer_price_in_country('US') AS average_beer_price;

-- Виклик процедури
CALL update_beer_price_based_on_rating();

-- Перевірка оновленої ціни
SELECT * FROM Beer;

-- Перевірка роботи тригера
UPDATE Beer SET alcohol_content = 4.8 WHERE id_beer = 1;
SELECT * FROM Beer_reviews WHERE id_beer = 1;
