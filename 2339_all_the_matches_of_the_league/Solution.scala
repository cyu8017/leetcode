// LeetCode 2339 - All the Matches of the League
// https:// leetcode.com/problems/all-the-matches-of-the-league/

object Solution {
  final val QUERY: String = """SELECT t1.team_name AS home_team, t2.team_name AS away_team
FROM
    Teams AS t1
    JOIN Teams AS t2
WHERE t1.team_name != t2.team_name
"""
}
