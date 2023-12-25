CREATE TABLE Breweries
(
  id_brewery INT NOT NULL,
  brewery_name VARCHAR(50) NOT NULL,
  Location VARCHAR(50) NOT NULL,
  year_of_establishment DATE NOT NULL,
  PRIMARY KEY (id_brewery)
);

CREATE TABLE Beer
(
  id_beer INT NOT NULL,
  beer_name VARCHAR(50) NOT NULL,
  type_of_beer VARCHAR(50) NOT NULL,
  alcohol_content FLOAT NOT NULL,
  country_of_origin VARCHAR(50) NOT NULL,
  price FLOAT NOT NULL,
  id_brewery INT NOT NULL,
  PRIMARY KEY (id_beer),
  FOREIGN KEY (id_brewery) REFERENCES Breweries(id_brewery)
);

CREATE TABLE Beer_reviews
(
  id_review INT NOT NULL,
  review_date DATE NOT NULL,
  author VARCHAR(50) NOT NULL,
  rating FLOAT NOT NULL,
  comment VARCHAR(100) NOT NULL,
  id_beer INT NOT NULL,
  PRIMARY KEY (id_review),
  FOREIGN KEY (id_beer) REFERENCES Beer(id_beer)
);
