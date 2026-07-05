# Leetcode 197: Rising temperature
# Difficulty : Easy
# Database : Mysql
  
SELECT w1.id
FROM Weather w1
join Weather w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;
