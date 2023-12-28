-- Записати нову ціну для пива на основі рейтингу
CREATE OR REPLACE PROCEDURE update_beer_price_based_on_rating()
LANGUAGE plpgsql
AS $$
BEGIN
    -- Оновити ціну на пиво за новими правилами
    UPDATE Beer
    SET price = CASE
                    WHEN alcohol_content >= 4.5 THEN price * 1.1 -- Збільшити ціну на 10% для високих рейтингів
                    WHEN alcohol_content >= 4.0 THEN price * 1.05 -- Збільшити ціну на 5% для середніх рейтингів
                    ELSE price -- Залишити ціну без змін для низьких рейтингів
                END;
END;
$$;

-- Виклик процедури
CALL update_beer_price_based_on_rating();

-- Перевірка оновленої ціни
SELECT * FROM Beer;
