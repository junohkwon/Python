drop table if exists book;
drop table if exists assign;
drop table if exists building_seat;
drop table if exists building;
drop table if exists performance;
drop table if exists audience;

create table building
(
	id	int auto_increment not null,
    name	varchar(200),
    location	varchar(200),
    capacity	int unsigned,
    primary key(id)
);

create table building_seat
(
	id	int not null,
    b_id	int not null,
    primary key(id, b_id),
    foreign key(b_id) references building(id) on delete cascade
)
;

create table performance
(
	id	int auto_increment not null,
    name	varchar(200),
    type	varchar(200),
    price	int unsigned,
    primary key(id)
);

create table audience
(
	id	int auto_increment not null,
    name	varchar(200),
    gender	char(2),
    age	int unsigned,
    primary key(id)
);

create table book
(
    a_id int not null,
	p_id int not null,
    seat_number int,
    primary key(a_id,p_id,seat_number),
    foreign key(a_id) references audience(id),
    foreign key(p_id) references performance(id)
)
;

create table assign
(
	p_id int not null,
	b_id int,
    primary key(p_id),
    foreign key(p_id) references performance(id),
    foreign key(b_id) references building(id)
);

insert into building (name, location, capacity) values ('Seoul Arts Center','Seoul',5);
insert into building (name, location, capacity) values ('Grand Peace Palace','Seoul',3);
insert into building (name, location, capacity) values ('Suwon Arts Center','Suwon',30);
insert into building (name, location, capacity) values ('Hwasung Arts Center','Hwasung',20);

insert into performance (name, type, price) values ('ColdPlay Concert','Concert', 100000);
insert into performance (name, type, price) values ('Jekyll & Hyde','Musical', 70000);
insert into performance (name, type, price) values ('Romeo and Juliet','Drama', 50000);
insert into performance (name, type, price) values ('Avengers','Movie', 10000);
insert into performance (name, type, price) values ('Star Wars','Movie', 12000);

insert into audience (name, gender, age) values ('Park Junghyuk','M',15);
insert into audience (name, gender, age) values ('Kim Taeuk','F',30);
insert into audience (name, gender, age) values ('Choi Jihun','M',56);
insert into audience (name, gender, age) values ('Shin Yoohyun','F',19);
insert into audience (name, gender, age) values ('Kwon hyun','M',36);


insert into building_seat values(1,1);
insert into building_seat values(2,1);
insert into building_seat values(3,1);
insert into building_seat values(4,1);
insert into building_seat values(5,1);


insert into building_seat values(1,2);
insert into building_seat values(2,2);
insert into building_seat values(3,2);


insert into building_seat values(1,3);
insert into building_seat values(2,3);
insert into building_seat values(3,3);
insert into building_seat values(4,3);
insert into building_seat values(5,3);
insert into building_seat values(6,3);
insert into building_seat values(7,3);
insert into building_seat values(8,3);
insert into building_seat values(9,3);
insert into building_seat values(10,3);
insert into building_seat values(11,3);
insert into building_seat values(12,3);
insert into building_seat values(13,3);
insert into building_seat values(14,3);
insert into building_seat values(15,3);
insert into building_seat values(16,3);
insert into building_seat values(17,3);
insert into building_seat values(18,3);
insert into building_seat values(19,3);
insert into building_seat values(20,3);
insert into building_seat values(21,3);
insert into building_seat values(22,3);
insert into building_seat values(23,3);
insert into building_seat values(24,3);
insert into building_seat values(25,3);
insert into building_seat values(26,3);
insert into building_seat values(27,3);
insert into building_seat values(28,3);
insert into building_seat values(29,3);
insert into building_seat values(30,3);

insert into building_seat values(1,4);
insert into building_seat values(2,4);
insert into building_seat values(3,4);
insert into building_seat values(4,4);
insert into building_seat values(5,4);
insert into building_seat values(6,4);
insert into building_seat values(7,4);
insert into building_seat values(8,4);
insert into building_seat values(9,4);
insert into building_seat values(10,4);
insert into building_seat values(11,4);
insert into building_seat values(12,4);
insert into building_seat values(13,4);
insert into building_seat values(14,4);
insert into building_seat values(15,4);
insert into building_seat values(16,4);
insert into building_seat values(17,4);
insert into building_seat values(18,4);
insert into building_seat values(19,4);
insert into building_seat values(20,4);


insert into assign values (1,1);
insert into assign values (2,1);
insert into assign values (3,1);
insert into assign values (4,3);
insert into assign values (5,4);

insert into book values (1,1,1);
insert into book values (1,1,2);
insert into book values (1,1,3);
insert into book values (1,1,4);
insert into book values (1,1,5);

insert into book values (2,1,6);
insert into book values (2,2,1);
insert into book values (2,2,2);
insert into book values (2,3,6);
insert into book values (2,4,9);

insert into book values (3,4,1);
insert into book values (3,4,2);
insert into book values (3,4,3);
insert into book values (3,4,4);
insert into book values (3,4,5);

insert into book values (4,1,7);
insert into book values (4,2,3);
insert into book values (4,3,3);


insert into book values (5,5,1);
insert into book values (5,5,2);
