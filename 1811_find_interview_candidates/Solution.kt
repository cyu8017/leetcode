// LeetCode 1811 - Find Interview Candidates
// https://leetcode.com/problems/find-interview-candidates/

class Solution {
    companion object {
        const val QUERY = "WITH Medals AS (\n" +
            "    SELECT contest_id, gold_medal AS user_id FROM Contests\n" +
            "    UNION ALL\n" +
            "    SELECT contest_id, silver_medal FROM Contests\n" +
            "    UNION ALL\n" +
            "    SELECT contest_id, bronze_medal FROM Contests\n" +
            "),\n" +
            "DistinctMedals AS (\n" +
            "    SELECT DISTINCT user_id, contest_id FROM Medals\n" +
            "),\n" +
            "ConsecutiveWinners AS (\n" +
            "    SELECT user_id\n" +
            "    FROM (\n" +
            "        SELECT\n" +
            "            user_id,\n" +
            "            contest_id - ROW_NUMBER() OVER (\n" +
            "                PARTITION BY user_id ORDER BY contest_id\n" +
            "            ) AS grp\n" +
            "        FROM DistinctMedals\n" +
            "    ) t\n" +
            "    GROUP BY user_id, grp\n" +
            "    HAVING COUNT(*) >= 3\n" +
            "),\n" +
            "GoldWinners AS (\n" +
            "    SELECT gold_medal AS user_id\n" +
            "    FROM Contests\n" +
            "    GROUP BY gold_medal\n" +
            "    HAVING COUNT(*) >= 3\n" +
            "),\n" +
            "Candidates AS (\n" +
            "    SELECT user_id FROM ConsecutiveWinners\n" +
            "    UNION\n" +
            "    SELECT user_id FROM GoldWinners\n" +
            ")\n" +
            "SELECT u.name, u.mail\n" +
            "FROM Users u\n" +
            "JOIN Candidates c ON u.user_id = c.user_id;"
    }
}
