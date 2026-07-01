# Leetcode 181 : Employees earning more then manager
# difficulty : Easy
# Database : Mysql

SELECT e.name AS employee
FROM employee e
JOIN employee m
ON e.managerId = m.id
WHERE e.salary > m.salary
