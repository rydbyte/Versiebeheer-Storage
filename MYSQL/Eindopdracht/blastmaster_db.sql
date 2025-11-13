create table game(
game_id int primary key,
game_name varchar(60),
genre varchar(30),
genre2 varchar(30),
price float
);

create table player(
player_id int primary key,
player_name varchar(50),
email varchar(50)
);

create table highscore(
game_id int,
player_id int,
pogingen int,
highscore int,
highscore_datum varchar(30),
foreign key (game_id) references game(game_id),
foreign key (player_id) references player(player_id)
);

create index game_id on game(game_id);

insert into game(game_id, game_name, genre,genre2, price)
values
(1,"Pac-Man", "Maze","Action", 1.50),
(2,"Space Invaders", "Shoot `em up","", 1.00),
(3,"Donkey Kong", "Platform","", 1.00), 
(4,"Street Fighter 11", "Fighting","", 1.00),
(5,"Galaga", "Shoot `em up","", 1.00),
(6,"Mortal Kombat", "Fighting","", 1.00),
(7,"Asteroids", "Shoot `em up","", 1.00),
(8,"Ms. Pac-Man", "Maze","Action", 1.50),
(9,"Frogger", "Action","Puzzle", 1.50),
(10,"Tetris", "Puzzle","", 1.00),
(11,"Defender", "Shoot `em up","", 1.00),
(12,"Dig-Dug", "Action","Puzzle", 1.50),
(13,"Bubble Bobble", "Platform","Puzzle", 1.50),
(14,"NBA Jam", "Sports","", 1.00),
(15,"Metal Slug", "Run and Gun","", 1.00),
(16,"Time Crisis", "Light Gun Shooter","", 1.00),
(17,"Q*bert", "Puzzle","Action", 1.50),
(18,"Rampage", "Action","", 1.00),
(19,"Track & Field", "Sports","", 1.00),
(20,"Contra", "Run and Gun","", 1.00);

insert into player(player_id, player_name, email)
values
(1, "Alex", "Alex@blastmaster.nova"),
(2, "Thomas", "Thomas@blastmaster.nova"),
(3, "Dani", "Dani@blastmaster.nova"),
(4, "Manoa", "Manoa@blastmaster.nova"),
(5, "Amber", "Amber@blastmaster.nova"),
(6, "Safoune", "Safoune@blastmaster.nova"),
(7, "Thijmen", "Thijmen@blastmaster.nova"),
(8, "Nikhil", "Nikhil@blastmaster.nova"),
(9, "Romy", "Romy@blastmaster.nova"),
(10, "Ryan", "Ryan@blastmaster.nova"),
(11, "Dean", "Dean@blastmaster.nova"),
(12, "Quinten", "Quinten@blastmaster.nova"),
(13, "Robert", "Robert@blastmaster.nova"),
(14, "Daniel", "Daniel@blastmaster.nova"),
(15, "Shane", "Shane@blastmasters.nova"),
(16, "Roxanne", "Roxanne@blastmaster.nova"),
(17, "Sander", "Sander@blastmasters.nova"),
(18, "Wouter", "Wouter@blastmaster.nova"),
(19, "Gregory", "Gregory@blastmaster.nova"),
(20, "Jeroen", "Jeroen@blastmaster.nova");