CREATE DATABASE IU_Jobly_DM;

USE IU_Jobly_DM;

-- Dimensiones

CREATE TABLE estudiantes (
    id_estudiante INT IDENTITY(1,1) PRIMARY KEY,
    nombre_completo NVARCHAR(255),
    correo NVARCHAR(255),
    departamento NVARCHAR(100),
    ciudad NVARCHAR(100),
    tiene_computador_internet BIT
);

CREATE TABLE academia (
    id_academia INT IDENTITY(1,1) PRIMARY KEY,
    programa_academico NVARCHAR(255),
    calidad_vinculacion NVARCHAR(100)
);

CREATE TABLE experiencia (
    id_experiencia INT IDENTITY(1,1) PRIMARY KEY,
    tiene_experiencia BIT,
    tiempo NVARCHAR(50),
    tipo_experiencia NVARCHAR(255),
    preferencias_tecnologicas NVARCHAR(255)
);

CREATE TABLE ingles (
    id_ingles INT IDENTITY(1,1) PRIMARY KEY,
    tiene_dominio BIT,
    nivel NVARCHAR(100)
);

CREATE TABLE comunicacion (
    id_comunicacion INT IDENTITY(1,1) PRIMARY KEY,
    plataformas NVARCHAR(255)
);

-- Hechos

CREATE TABLE participacion (
    id_participacion INT IDENTITY(1,1) PRIMARY KEY,
    id_estudiante INT,
    id_academia INT,
    id_experiencia INT,
    id_ingles INT,
    id_comunicacion INT,
    interesado_participar BIT,
    fecha DATETIME,
    FOREIGN KEY (id_estudiante) REFERENCES estudiantes(id_estudiante),
    FOREIGN KEY (id_academia) REFERENCES academia(id_academia),
    FOREIGN KEY (id_experiencia) REFERENCES experiencia(id_experiencia),
    FOREIGN KEY (id_ingles) REFERENCES ingles(id_ingles),
    FOREIGN KEY (id_comunicacion) REFERENCES comunicacion(id_comunicacion)
);
