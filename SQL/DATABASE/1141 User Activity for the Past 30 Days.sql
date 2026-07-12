# Leetcode 1141: User activity for the past 30 days
# Difficulty : Easy
# Database : Mysql
  
SELECT 
    activity_date AS day,
    COUNT(DISTINCT user_id) AS
active_users
FROM Activity
WHERE activity_date BETWEEN
'2019-06-28' AND '2019-07-27'
GROUP BY activity_date;
