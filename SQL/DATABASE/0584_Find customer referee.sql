# Leetcode 584: Find Customer Referee
# Difficulty : Easy
# Database : Mysql
  
SELECT name
FROM Customer
WHERE referee_id != 2
    OR referee_id IS NULL;
