# Leetcode 176 : Second Highest Salary
# Difficulty : Medium
# Database : Mysql

SELECT (
    SELECT DISTINCT salary 
    FROM employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET 1
) AS secondhighestsalary;
