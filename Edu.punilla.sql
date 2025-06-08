
CREATE DATABASE IF NOT EXISTS sistem_usuarios;
USE sistem_usuarios;
CREATE TABLE roles (
    id INT AUTO_INCREMENT PRIMARY KEY,            
    nombre_rol VARCHAR(50) NOT NULL UNIQUE);
INSERT INTO roles (nombre_rol) VALUES 
('admin'), 
('usuario_estándar');
CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,             
    nombre VARCHAR(100) NOT NULL,                
    email VARCHAR(100) NOT NULL UNIQUE,            
    contraseña VARCHAR(255) NOT NULL,              
    rol_id INT NOT NULL,                           
    estado ENUM('activo', 'inactivo') DEFAULT 'activo',  
    FOREIGN KEY (rol_id) REFERENCES roles(id)
    );



