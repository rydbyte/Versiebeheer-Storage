-- opdracht 1 deel 1
select * from pokemon where name = "bulbasaur" or name = "zapdos" or name = "steelix" or name = "elekid" or name = "regice" or name = "magnezone" or name = "walrein";

select * from pokemon order by weight desc limit 3;
select * from pokemon order by weight asc limit 3;

select * from pokemon order by base_experience asc limit 3;
select * from pokemon order by base_experience desc limit 3;

select count(id) from pokemon;
select avg(height) from pokemon;
select sum(weight) from pokemon;

-- opdracht 1 deel 2
select * from pokemon 
join pokemon_types
on pokemon_types.pokemon_id = pokemon.id
join types
on types.id = pokemon_types.type_id where pokemon.name = "gengar" or pokemon.name = "charizard" or pokemon.name = "kraby"
or pokemon.name = "flygon" or pokemon.name = "milotic" or pokemon.name = "duskskull" or pokemon.id = 412 or pokemon.name = "noibat";

select * from pokemon
join pokemon_types
on pokemon_types.pokemon_id = pokemon.id
join types
on types.id = pokemon_types.type_id
where types.name = "ground"
order by weight desc limit 3;

select * from pokemon
join pokemon_types
on pokemon_types.pokemon_id = pokemon.id
join types
on types.id = pokemon_types.type_id
where types.name = "ghost"
order by weight asc limit 3;

select * from pokemon
join pokemon_types
on pokemon_types.pokemon_id = pokemon.id
join types
on types.id = pokemon_types.type_id
where types.name = "bug"
order by base_experience asc limit 3;

select * from pokemon
join pokemon_types
on pokemon_types.pokemon_id = pokemon.id
join types
on types.id = pokemon_types.type_id
where types.name = "dragon"
order by base_experience desc limit 3;

select pokemon.name, base_stats.defense from pokemon
join base_stats
on base_stats.pokemon_id = pokemon.id
order by base_stats.defense desc limit 1;

select pokemon.name, base_stats.attack from pokemon
join base_stats
on base_stats.pokemon_id = pokemon.id
order by base_stats.defense asc limit 1;

select pokemon.name, base_stats.speed, types.name from pokemon
join base_stats
on base_stats.pokemon_id = pokemon.id
join pokemon_types
on pokemon_types.pokemon_id = pokemon.id
join types
on types.id = pokemon_types.type_id
where types.name = "electric"
order by base_stats.speed desc limit 1;

select avg(base_stats.special_attack) from pokemon
join base_stats
on base_stats.pokemon_id = pokemon.id
join pokemon_types
on pokemon_types.pokemon_id = pokemon.id
join types
on types.id = pokemon_types.type_id
where types.name = "psychic";

select count(types.name), types.name from pokemon
join pokemon_types
on pokemon_types.pokemon_id = pokemon.id
join types
on types.id = pokemon_types.type_id
group by types.name 
order by count(types.name) desc;


