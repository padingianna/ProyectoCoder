-- SQLite
-- SQLite
/*DELETE FROM Home_destino WHERE id is not null;
SELECT * FROM Home_hotel;
-- SQLite*/
select * from Home_excursiones;

/*insert into Home_excursiones (
        e_lugar, 
e_dias ,
e_actividad ,
e_dificultad ,
e_salida ,
e_regreso ,
e_costo )

VALUES


('Balcarce,Buenos Aires',9,'Cabalgata','Media','2022-9-4','2022-9-13',261),
('Mar del Plata,Buenos Aires',17,'Caminata','Baja','2022-3-5','2022-3-22',67),
('Sierra de los Padres,Buenos Aires',19,'Cabalgata','Media','2022-5-25','2022-6-14',281),
('Tinogasta,Catamarca',2,'Paseo en 4x4','Alta','2022-4-13','2022-4-15',146),
('Resistencia,Chaco',17,'Paseo en 4x4','Alta','2022-4-16','2022-5-3',292),
('El Hoyo,Chubut',3,'Cabalgata','Media','2022-12-4','2022-12-7',44),
('Villa Futalaufquen,Chubut',17,'Paseo en 4x4','Alta','2022-11-14','2022-11-1',329),
('Alta Gracia,Cordoba',23,'Caminata','Baja','2022-11-26','2022-12-19',82),
('Cordoba Capital,Cordoba',11,'Caminata','Baja','2022-2-24','2022-3-5',252),
('Jesus Maria,Cordoba',25,'Caminata','Baja','2022-8-25','2022-9-21',81),
('Villa Carlos Paz,Cordoba',18,'Caminata','Baja','2022-7-17','2022-8-5',345),
('Gualeguaychu,Entre Rios',21,'Paseo en 4x4','Alta','2022-6-5','2022-6-26',217),
('Humahuaca,Jujuy',22,'Caminata','Baja','2022-5-29','2022-6-21',271),
('San Salvador de Jujuy,Jujuy',24,'Circuito Historico','Baja','2022-4-12','2022-5-6',112),
('La Rioja Capital,La Rioja',22,'Paseo en 4x4','Alta','2022-6-6','2022-6-28',181),
('San Rafael,Mendoza',24,'Caminata','Baja','2022-7-11','2022-8-5',32),
('Puerto Iguazu,Misiones',17,'Caminata','Baja','2022-6-28','2022-7-15',315),
('Villa La Angostura,Neuquen',13,'Caminata','Baja','2022-1-5','2022-1-18',122),
('San Martin de los Andes,Neuquen',3,'Paseo en 4x4','Alta','2022-4-24','2022-4-27',221),
('Las Grutas,Rio Negro',7,'Circuito Historico','Baja','2022-4-21','2022-4-27',71),
('San Andres de los Cobres,Salta',25,'Caminata','Baja','2022-8-28','2022-9-23',23),
('Merlo,San Luis',14,'Circuito Historico','Baja','2022-11-3','2022-11-17',247),
('Ushuaia,Tierra del Fuego',8,'Caminata','Baja','2022-1-14','2022-1-22',183),
('Tafi del Valle,Tucuman',5,'Paseo en 4x4','Alta','2022-6-6','2022-6-11',155),
('Bariloche,Rio Negro',6,'Circuito Historico','Baja','2022-5-5','2022-5-11',73);