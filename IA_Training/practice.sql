select * from sakila.actor;
use world;
select * from country;
select count(population) from country where population>1000000000;
SELECT COUNT(population) FROM country;	
show tables;
use northwind;
show tables;
select * from orders;
select min(employeeid) from orders;
select productid from products order by unitsonorder desc;
select avg(freight) from orders;
select sum(freight) from orders;


