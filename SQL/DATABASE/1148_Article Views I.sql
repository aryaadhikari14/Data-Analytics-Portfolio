# Leetcode 1148: Article Views I
# Difficulty : Easy
# Database : Mysql

SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
