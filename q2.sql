SELECT name FROM salesperson, orders WHERE salesperson_id=id GROUP BY salesperson_id HAVING COUNT (*) >1;
