CREATE DATABASE sistema_login;

USE sistema_login;

CREATE TABLE usuarios (

    id INT AUTO_INCREMENT PRIMARY KEY,

    usuario VARCHAR(100) NOT NULL UNIQUE,

    senha VARCHAR(255) NOT NULL

);

INSERT INTO usuarios (usuario, senha)
VALUES ('admin', '123456');