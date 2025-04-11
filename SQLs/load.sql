-- 1. Insertar estudiantes
INSERT INTO estudiantes (nombre_completo, correo, departamento, ciudad, tiene_computador_internet)
SELECT DISTINCT 
    nombre_completo, 
    COALESCE(correo_2, correo_1), 
    departamento, 
    ciudad,
    CASE WHEN tiene_computador_internet LIKE '%sí%' THEN 1 ELSE 0 END
FROM formulario_raw;

-- 2. Insertar academia
INSERT INTO academia (programa_academico, calidad_vinculacion)
SELECT DISTINCT programa_academico, calidad_vinculacion
FROM formulario_raw;

-- 3. Insertar experiencia
INSERT INTO experiencia (tiene_experiencia, tiempo, tipo_experiencia, preferencias_tecnologicas)
SELECT DISTINCT 
    CASE WHEN experiencia_ti LIKE '%sí%' THEN 1 ELSE 0 END,
    tiempo_experiencia,
    tipo_experiencia,
    preferencias_tecnologicas
FROM formulario_raw;

-- 4. Insertar ingles
INSERT INTO ingles (tiene_dominio, nivel)
SELECT DISTINCT 
    CASE WHEN dominio_ingles LIKE '%sí%' THEN 1 ELSE 0 END,
    nivel_ingles
FROM formulario_raw;

-- 5. Insertar comunicación
INSERT INTO comunicacion (plataformas)
SELECT DISTINCT plataformas_contacto
FROM formulario_raw;

-- 6. Insertar hechos
INSERT INTO participacion (
    id_estudiante, id_academia, id_experiencia, id_ingles, id_comunicacion, interesado_participar, fecha
)
SELECT 
    e.id_estudiante,
    a.id_academia,
    ex.id_experiencia,
    i.id_ingles,
    c.id_comunicacion,
    CASE WHEN r.interesado_participar LIKE '%sí%' THEN 1 ELSE 0 END,
    r.marca_temporal
FROM formulario_raw r
JOIN estudiantes e ON e.nombre_completo = r.nombre_completo
JOIN academia a ON a.programa_academico = r.programa_academico AND a.calidad_vinculacion = r.calidad_vinculacion
JOIN experiencia ex ON ex.tipo_experiencia = r.tipo_experiencia AND ex.tiempo = r.tiempo_experiencia
JOIN ingles i ON i.nivel = r.nivel_ingles
JOIN comunicacion c ON c.plataformas = r.plataformas_contacto;
