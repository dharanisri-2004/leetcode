/*select name,bonus from Employee e
left join bonus b on e.empid=b.empid
where bonus<1000 or bonus is null;*/
select name,bonus from bonus b
right join Employee e on e.empid=b.empid
where bonus<1000 or bonus is null;