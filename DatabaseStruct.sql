CREATE SCHEMA `books` ;

CREATE TABLE `books`.`books` (
  `title` VARCHAR(512) NOT NULL,
  `author` VARCHAR(512) NULL,
  `rating` FLOAT NULL,
  `complete_link` VARCHAR(512) NULL);
