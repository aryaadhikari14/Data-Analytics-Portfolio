# Leetcode 1378: Replace employee ID with the unique identifier
# Difficulty : Easy
# Database : Mysql
  
SELECT 
    eu.unique_id,
    e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
ON e.id = eu.id;
