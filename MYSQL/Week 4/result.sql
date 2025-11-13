select * from snack;
select * from menu;

select avg(prijs) from snack;
select avg(prijs_toelage) from menu;
select * from menu where bevat_frietjes = false;
select * from snack join menu on menu.snack = snack.naam where snack.vegetarisch = true;
select count(menu.snack) as 'value_occurrence', snack.naam from menu join snack on snack.naam = menu.snack group by menu.snack order by 'value_occurrence' desc




