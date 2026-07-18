# Leetcode 619: Biggest single number
# Difficulty : Easy
# Database : Mysql
  
SELECT MAX(num) AS num
FROM (
    SELECT num 
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS t;
