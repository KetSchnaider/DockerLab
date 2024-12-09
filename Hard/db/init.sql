CREATE DATABASE IF NOT EXISTS procesare_db;

USE procesare_db;

CREATE TABLE IF NOT EXISTS processed_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    original TEXT NOT NULL,
    length INT NOT NULL,
    reversed TEXT NOT NULL,
    uppercased TEXT NOT NULL,
    words TEXT NOT NULL
);
