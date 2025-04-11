CREATE DATABASE IU_Jobly_Form;

USE IU_Jobly_Form;

CREATE TABLE formulario_raw (
    id INT IDENTITY(1,1) PRIMARY KEY,
    marca_temporal DATETIME,
    correo_1 NVARCHAR(255),
    correo_2 NVARCHAR(255),
    nombre_completo NVARCHAR(255),
    departamento NVARCHAR(100),
    ciudad NVARCHAR(100),
    programa_academico NVARCHAR(255),
    calidad_vinculacion NVARCHAR(100),
    experiencia_ti NVARCHAR(10),
    tiempo_experiencia NVARCHAR(50),
    tipo_experiencia NVARCHAR(255),
    preferencias_tecnologicas NVARCHAR(255),
    dominio_ingles NVARCHAR(10),
    nivel_ingles NVARCHAR(100),
    plataformas_contacto NVARCHAR(255),
    tiene_computador_internet NVARCHAR(10),
    interesado_participar NVARCHAR(10)
);
