create database ria_drm;

use ria_drm;

create table clientes(
    nombre_cli varchar(30) not null primary key,
    ape_pa varchar(20) not null,
    ape_ma varchar(20) not null,
    empresa varchar(10) not null,
    email varchar(50) not null
    )ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into clientes (nombre_cli, ape_pa, ape_ma, empresa, email) values 
('Daniela', 'Rubiales', 'Marquez', 'kiro', 'dani@gmail.com'),
('Jesus', 'Calderon', 'Hernandez', 'pucca', 'puca@gmail.com'),
('Diego', 'Borda', 'Epinoza', 'cordoba', 'cesar@gmail.com');

create table productos(
    id_pro varchar(5) not null primary key,
    nom_p varchar(30) not null,
    cantidad int not null,
    fecha date not null,
    precio double not null
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

insert into productos(id_pro, nom_p, cantidad, fecha, precio) values
('01', 'Goma', 2, '2019/01/10', 8.0),
('02', 'Libreta', 1, '2019/02/11', 13.0),
('03', 'Resistol', 1, '2019/04/03', 7.0);


create user 'ria'@'localhost' identified by 'ria.2019';
grant all privileges on ria_drm.* to 'ria'@'localhost';
flush privileges; 