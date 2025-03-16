#select product_id, year first_year, quantity, price from Sales
#where (product_id, year) in (select product_id, min(year)from Sales group by 1);

select product_id, year first_year, quantity, price
from (select *, rank() over (partition by product_id order by year) rk from Sales)t
where rk = 1