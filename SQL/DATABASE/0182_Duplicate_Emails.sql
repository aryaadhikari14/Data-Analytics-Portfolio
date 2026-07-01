# Leetcode 182: Duplicate emails
# Difficulty : Easy
# Database : Mysql

SELECT email AS Email
FROM person
GROUP BY email
HAVING COUNT(*) > 1;
