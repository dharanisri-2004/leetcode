select customer_id from Customer group by 1
having count(distinct product_key)=(select count(*) from Product);