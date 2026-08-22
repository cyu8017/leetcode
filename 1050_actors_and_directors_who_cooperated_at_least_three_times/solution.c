// LeetCode 1050 - Actors and Directors Who Cooperated At Least Three Times
// https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/

const char* QUERY =
    "\n"
    "SELECT actor_id, director_id\n"
    "FROM ActorDirector\n"
    "GROUP BY actor_id, director_id\n"
    "HAVING COUNT(*) >= 3\n";
