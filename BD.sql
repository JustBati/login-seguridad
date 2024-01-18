-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS BD;
USE BD;

-- Crear tabla 'Maquinas'
CREATE TABLE IF NOT EXISTS Maquinas (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Tipo VARCHAR(30),
    Marca VARCHAR(10),
    Modelo VARCHAR(30),
    No_Serie VARCHAR(10),
    Observaciones VARCHAR(50)
);

-- Crear tabla 'Usuario'
CREATE TABLE IF NOT EXISTS Usuario (
    Nombre VARCHAR(30) PRIMARY KEY,
    Contraseña VARCHAR(30) NOT NULL,
    UNIQUE (Nombre) -- Asegura que el nombre de usuario sea único
);

-- Crear tabla 'Prestamos'
CREATE TABLE IF NOT EXISTS Prestamos (
    id_maquina INT,
    id_usuario VARCHAR(30),
    FOREIGN KEY (id_maquina) REFERENCES Maquinas(ID),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(Nombre)
    -- Considerar agregar una columna 'id' como PRIMARY KEY si se anticipa que cada préstamo debe ser único
);