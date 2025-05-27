-- Query to generate total sales in a month
SELECT SUM(amount) AS total_sales
FROM orders
WHERE strftime('%m', "order_date") = '03';



--Query to get the highest customer
SELECT customer, SUM(amount) AS total_spent
FROM orders
GROUP BY customer
ORDER BY total_spent DESC
LIMIT 1;


--Query to get the average order value for the last three months.
SELECT AVG(amount) AS avg_order_value
FROM orders
WHERE "order_date" <= date('now', '-3 months');

