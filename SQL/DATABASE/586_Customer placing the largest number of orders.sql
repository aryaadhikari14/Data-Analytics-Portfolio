# Leetcode 586: Customer placing the largest number of orders
# Difficulty : Easy
# Database : Mysql
  
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1; 
