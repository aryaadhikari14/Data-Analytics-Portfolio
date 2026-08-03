# Leetcode 1527: Patients with a condition
# Difficulty : Easy
# Database : Mysql

SELECT *
FROM Patients
WHERE conditions LIKE 'DIAB1%'
   OR conditions LIKE '% DIAB1%';
