-- Створення тригера для оновлення рейтингу в відгуках при оновленні alcohol_content в таблиці Beer
CREATE OR REPLACE FUNCTION update_rating_trigger()
RETURNS TRIGGER AS $$
BEGIN
    -- Оновлення рейтингу у відгуках
    UPDATE Beer_reviews
    SET rating = NEW.alcohol_content
    WHERE id_beer = NEW.id_beer;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Додавання тригера до таблиці Beer
CREATE TRIGGER beer_update_trigger
AFTER UPDATE OF alcohol_content ON Beer
FOR EACH ROW
EXECUTE FUNCTION update_rating_trigger();

-- Перевірка роботи тригера
UPDATE Beer SET alcohol_content = 4.8 WHERE id_beer = 1;
SELECT * FROM Beer_reviews WHERE id_beer = 1;
