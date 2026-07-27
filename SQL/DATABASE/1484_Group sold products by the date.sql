#Leetcode 1484: Group sold products by the date
# Difficulty : Easy
# Database : Mysql
  
SELECT
    sell_date,
    COUNT(DISTINCT product) AS 
num_sold,
    GROUP_CONCAT(DISTINCT
product ORDER BY product
SEPARATOR ',') AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;
