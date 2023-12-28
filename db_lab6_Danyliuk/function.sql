DROP FUNCTION IF EXISTS avg_beer_price_in_country(country_code VARCHAR);
CREATE OR REPLACE FUNCTION avg_beer_price_in_country(country_code VARCHAR)
RETURNS DECIMAL AS
$$
DECLARE
    avg_price DECIMAL;
BEGIN
    -- Обчислення середньої ціни пива за відгуками у вказаній країні
    SELECT AVG(price) INTO avg_price
    FROM Beer
    WHERE country_of_origin = country_code;

    -- Повернення результату
    RETURN COALESCE(avg_price, 0);  -- Враховуємо випадок, коли немає записів
END;
$$
LANGUAGE plpgsql;


-- Виклик функції
SELECT avg_beer_price_in_country('US') AS average_beer_price;
