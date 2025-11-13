create table snack(
naam varchar(50) primary key,
prijs float,
voorraad int,
vegetarisch boolean
);

create index index_snack_naam on snack(naam);

create table menu(
naam varchar(50) primary key,
prijs_toelage float,
snack varchar(50),
bevat_frietjes boolean,
foreign key (snack) references snack(naam)
);

