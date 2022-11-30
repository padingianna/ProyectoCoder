-- SQLite
/*DELETE FROM Home_destino WHERE id is not null;
SELECT * FROM Home_hotel;*/
-- SQLite
select * from Home_hotel;
/*
insert into Home_hotel (
    h_destino,
    h_lugar,
    h_dias,
    h_pension,
    h_habitacion,
    h_ingreso,
    h_salida,
    h_costo)

VALUES


('Balcarce,Buenos Aires',               'Hilton',9,'Media (desayuno y Cena)',               'Doble','2022-9-4','2022-9-13',261),
('Mar del Plata,Buenos Aires',          'Sheraton',17,'Completa',                   'Simple','2022-3-5','2022-3-22',67),
('Sierra de los Padres,Buenos Aires',   'NH',19,'Media (desayuno y Cena)',              'Triple','2022-5-25','2022-6-14',281),
('Tinogasta,Catamarca',                 'Hilton',2,'Desayuno',                      'Doble','2022-4-13','2022-4-15',146),
('Resistencia,Chaco',                   'Hilton',17,'Desayuno',                     'Doble','2022-4-16','2022-5-3',292),
('El Hoyo,Chubut',                      'Sheraton',3,'Media (desayuno y Cena)',             'Doble','2022-12-4','2022-12-7',44),
('Villa Futalaufquen,Chubut',           'NH',17,'Desayuno',                             'Doble','2022-11-14','2022-11-1',329),
('Alta Gracia,Cordoba',                 'Hilton',23,'Completa',                             'Simple','2022-11-26','2022-12-19',82),
('Cordoba Capital,Cordoba',             'Sheraton',11,'Completa',                'Triple','2022-2-24','2022-3-5',252),
('Jesus Maria,Cordoba',                 'NH',25,'Completa',                         'Doble','2022-8-25','2022-9-21',81),
('Villa Carlos Paz,Cordoba',            'Trinidad',18,'Completa',                   'Simple','2022-7-17','2022-8-5',345),
('Gualeguaychu,Entre Rios',             'Hilton',21,'Desayuno',                     'Doble','2022-6-5','2022-6-26',217),
('Humahuaca,Jujuy',                     'Hilton',22,'Completa',                     'Triple','2022-5-29','2022-6-21',271),
('San Salvador de Jujuy,Jujuy',         'Sheraton',24,'Media (desayuno y Cena)',                'Doble','2022-4-12','2022-5-6',112),
('La Rioja Capital,La Rioja',           'Hilton',22,'Desayuno',                     'Triple','2022-6-6','2022-6-28',181),
('San Rafael,Mendoza',                  'Hilton',24,'Completa',                     'Doble','2022-7-11','2022-8-5',32),
('Puerto Iguazu,Misiones',              'Hilton',17,'Completa',                 'Simple','2022-6-28','2022-7-15',315),
('Villa La Angostura,Neuquen',          'Hilton',13,'Completa',                     'Doble','2022-1-5','2022-1-18',122),
('San Martin de los Andes,Neuquen',     'Sheraton',3,'Desayuno',                'Triple','2022-4-24','2022-4-27',221),
('Las Grutas,Rio Negro',                'Hilton',7,'Media (desayuno y Cena)',               'Doble','2022-4-21','2022-4-27',71),
('San Andres de los Cobres,Salta',      'Hilton',25,'Completa',                     'Doble','2022-8-28','2022-9-23',23),
('Merlo,San Luis',                      'Hilton',14,'Media (desayuno y Cena)',      'Simple','2022-11-3','2022-11-17',247),
('Ushuaia,Tierra del Fuego',            'Hilton',8,'Completa',                      'Doble','2022-1-14','2022-1-22',183),
('Tafi del Valle,Tucuman',              'Hilton',5,'Desayuno',                      'Doble','2022-6-6','2022-6-11',155),
('Bariloche,Rio Negro',                 'Hilton',6,'Media (desayuno y Cena)',               'Triple','2022-5-5','2022-5-11',73);