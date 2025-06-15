-- 1. Calculate the total sales volume for March 2024
SELECT SUM(amount) as total_sales_march_2024
FROM orders
WHERE order_date >= '2024-03-01' AND order_date <= '2024-03-31';

-- 2. Find the customer who spent the most overall
SELECT customer, SUM(amount) as total_spent
FROM orders
GROUP BY customer
ORDER BY total_spent DESC
LIMIT 1;

-- 3. Calculate the average order value for the last three months
SELECT AVG(amount) as average_order_value
FROM orders
WHERE order_date >= date('2024-03-30', '-3 months'); 