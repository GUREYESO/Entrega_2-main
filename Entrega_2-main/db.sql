-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS Entrega_2;
USE Entrega_2;

-- Crear tabla ciudades
CREATE TABLE ciudades (
    ciud_id INT AUTO_INCREMENT PRIMARY KEY,
    ciud_nombre VARCHAR(255) NOT NULL
);

-- Crear tabla personas
CREATE TABLE personas (
    dir_tel INT PRIMARY KEY,
    dir_tipo_tel VARCHAR(20),
    dir_nombre VARCHAR(255),
    dir_direccion VARCHAR(255),
    dir_ciud_id INT,
    FOREIGN KEY (dir_ciud_id) REFERENCES ciudades(ciud_id)
);

-- Insertar datos de prueba en la tabla ciudades
INSERT INTO ciudades (ciud_nombre) VALUES
('Bogotá'),
('Medellín'),
('Cali'),
('Barranquilla'),
('Cartagena');

-- Insertar datos de prueba en la tabla personas
INSERT INTO personas (dir_tel, dir_tipo_tel, dir_nombre, dir_direccion, dir_ciud_id) VALUES
(3150111111, 'Casa', 'John Doe', '123 Main St', 1),
(3150222222, 'Trabajo', 'Jane Smith', '456 Park Ave', 2),
(3150333333, 'Casa', 'Michael Johnson', '789 Elm St', 3),
(3150444444, 'Trabajo', 'Emily Davis', '101 Pine St', 4),
(3150555555, 'Casa', 'David Wilson', '202 Oak Ave', 5);