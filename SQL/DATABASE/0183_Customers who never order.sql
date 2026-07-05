# Leetcode 183: Customers who never order
# Difficulty : Easy
# Database : Mysql
  
SELECT c.name AS customers
FROM customers c
LEFT JOIN orders o
ON c.id = o.customerId
WHERE o.customerId is NULL;
