// LeetCode 1050 - Actors And Directors Who Cooperated At Least Three Times
// https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/

class Solution {
    companion object {
        const val QUERY = "SELECT actor_id, director_id\n" +
            "FROM ActorDirector\n" +
            "GROUP BY actor_id, director_id\n" +
            "HAVING COUNT(*) >= 3"
    }
}
