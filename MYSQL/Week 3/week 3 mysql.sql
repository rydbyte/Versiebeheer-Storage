/* opdr 1 popplio*/
update pokemon 
set 
height = 1, 
weight = 8, 
base_experience = 20 
where id = 722;

select * from pokemon where id = 722;

/* opdr 2 change id charizard*/
update types join pokemon_types
on pokemon_types.type_id = types.id
set
types.name = "dragon"
where pokemon_types.type_id = 3;

select * from pokemon
join pokemon_types
on pokemon_types.pokemon_id = pokemon.id
join types
on types.id = pokemon_types.type_id
where pokemon.name = "charizard";

/* opdr 3 insert wouter*/
insert into pokemon(id,name,height,weight,base,experience)
values(723, woutorio, 50, 80, 30);

insert into pokemon_types(pokemon_id, type_id, slot)
values(723, 15, 2);

insert into pokemon_types(pokemon_id, type_id, slot)
values(723, 13, 1);

/* opdr 4 beard type*/
insert into types(id, name)
values(19, beard);

insert into pokemon(id,name,height,weight,base,experience)
values(724, curlyboy, 50, 80, 30);

insert into pokemon_types(pokemon_id, type_id, slot)
values(724, 19, 1);

insert into pokemon(id,name,height,weight,base,experience)
values(725, goateedude, 50, 80, 30);

insert into pokemon_types(pokemon_id, type_id, slot)
values(725, 19, 1);

insert into pokemon(id,name,height,weight,base,experience)
values(726, beardman, 50, 80, 30);

insert into pokemon_types(pokemon_id, type_id, slot)
values(725, 19, 1);

insert into pokemon_types(pokemon_id, type_id, slot)
values(725, 17, 1);

select * from pokemon 
order by id desc;

select * from pokemon_types join types
on pokemon_types.type_id = types.id
order by pokemon_id desc;

select * from types;

#ik had de inserts gedelete omdat ze anders dupliceerde '-'

