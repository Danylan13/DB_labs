-- loop.sql

DO $$
DECLARE
    i INT;
BEGIN
    FOR i IN 1..20 LOOP
        INSERT INTO Breweries (id_brewery, brewery_name, Location, year_of_establishment)
        VALUES (i, 'Brewery' || i, 'Location' || i, '2023-01-01');
    END LOOP;
END $$;

-- Розкоментуйте наступні рядки, щоб побачити вставлені дані
-- SELECT * FROM Breweries;
-- DELETE FROM Breweries WHERE year_of_establishment = '2023-01-01';
-- SELECT * FROM Breweries;
