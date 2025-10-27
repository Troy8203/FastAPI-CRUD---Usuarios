CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    fecha_nacimiento DATE,
    telefono VARCHAR(20),
    direccion VARCHAR(150)
);

INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, telefono, direccion)
VALUES ('Juan', 'Pérez', '1990-05-12', '555123456', 'Calle Falsa 123');

INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, telefono, direccion)
VALUES ('María', 'Gómez', '1985-11-23', '555987654', 'Avenida Siempre Viva 456');

INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, telefono, direccion)
VALUES ('Carlos', 'López', '1992-07-15', '555111222', 'Calle Luna 78');

INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, telefono, direccion)
VALUES ('Ana', 'Martínez', '1988-02-28', '555333444', 'Plaza Mayor 5');

INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, telefono, direccion)
VALUES ('Luis', 'Ramírez', '1995-09-10', '555555666', 'Calle Sol 22');

INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, telefono, direccion)
VALUES ('Sofía', 'Torres', '1991-12-01', '555777888', 'Avenida del Mar 9');

INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, telefono, direccion)
VALUES ('Miguel', 'Hernández', '1989-03-20', '555999000', 'Calle Verde 14');

INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, telefono, direccion)
VALUES ('Laura', 'Vargas', '1993-08-18', '555121212', 'Avenida Central 33');

INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, telefono, direccion)
VALUES ('Diego', 'Santos', '1994-06-05', '555343434', 'Calle Naranja 21');

INSERT INTO usuarios (nombre, apellido, fecha_nacimiento, telefono, direccion)
VALUES ('Elena', 'Ruiz', '1990-11-30', '555565656', 'Plaza Nueva 7');
