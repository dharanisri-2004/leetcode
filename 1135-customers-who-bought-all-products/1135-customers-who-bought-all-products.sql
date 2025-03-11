select customer_id from Customer group by 1
having COUNT(distinct product_key)=(select COUNT(*) from Product);