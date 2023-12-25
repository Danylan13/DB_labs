INSERT INTO Breweries (id_brewery, brewery_name, location, year_of_establishment)
VALUES
(1, 'Brighton Beer Dispensary', 'Brighton, GB', '1990-01-15'),
(2, 'Coachella Valley Brewing Co', 'Thousand Palms, US', '2005-07-21'),
(3, 'Broadway Wine Merchant', 'Oklahoma City, US', '2010-03-04'),
(4, 'Bistro Europa/House Of Klaus', 'Alexandria, US', '1995-11-08'),
(5, 'Le Bien, Le Malt', 'Rimouski, CA', '2001-08-22'),
(6, 'Redneck Gourmet', 'Newnan, US', '2005-03-13'),
(7, 'TЕ™ebonickГЅ RukodД›lnГЅ PivovГЎrek', 'Praha, CZ', '2015-05-12');


INSERT INTO Beer (id_beer, beer_name, type_of_beer, alcohol_content, country_of_origin, price, id_brewery)
VALUES
(1, 'MegaMeow Imperial Stout', 'Imperial Stout', 4.5, 'US', 2.99, 1),
(2, 'World Burp Beer 2002', 'Japanese Rice Lager, Limited ((brewed once)', 6.2, 'JP', 3.49, 2),
(3, 'Icon Sender', 'American Lager', 5.8, 'US', 4.29, 3),
(4, 'Belgian Style Wit', 'Belgian Witbier', 4.7, 'US', 3.99, 4),
(5, 'The Sky Is High ((wet Hopped Pale Ale)', 'American Pale Ale ((APA)', 6.0, 'US', 4.59, 5),
(6, 'Schwartz Hop', 'American Black Ale', 6.0, 'US', 5.29, 6),
(7, 'Bojan Wielkopolskie', 'European Pale Lager', 5.0, 'PL', 4.99, 7);


INSERT INTO Beer_reviews (id_review, review_date, author, rating, comment, id_beer)
VALUES
(1, '2023-03-10', 'John Doe', 4.5, 'A great beer with a rich flavor.', 1),
(2, '2023-03-11', 'Jane Smith', 4.2, 'Smooth and balanced taste.', 2),
(3, '2023-03-12', 'Mike Johnson', 3.8, 'Not bad, but could be better.', 3),
(4, '2023-03-13', 'Sarah Brown', 4.7, 'Excellent stout, love it!', 4),
(5, '2023-03-14', 'David Lee', 4.9, 'Outstanding porter, worth trying.', 5),
(6, '2023-03-15', 'Emily White', 3.5, 'Decent beer, could use more flavor.', 6),
(7, '2023-03-16', 'Robert Green', 4.0, 'Enjoyable APA with a hoppy profile.', 7);
