# Leetcode 1050: Actors and directors who cooperated at least three times
# Difficulty : Easy
# Database : Mysql
  
SELECT 
    actor_id,
    director_id
FROM ActorDirector 
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;
