// LeetCode 2339 - All The Matches Of The League
// https://leetcode.com/problems/all-the-matches-of-the-league/

class Solution {
    companion object {
        const val QUERY = "SELECT t1.team_name AS home_team, t2.team_name AS away_team\n" +
            "FROM\n" +
            "    Teams AS t1\n" +
            "    JOIN Teams AS t2\n" +
            "WHERE t1.team_name != t2.team_name"
    }
}
