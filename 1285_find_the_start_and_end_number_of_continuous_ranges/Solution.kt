// LeetCode 1285 - Find The Start And End Number Of Continuous Ranges
// https://leetcode.com/problems/find-the-start-and-end-number-of-continuous-ranges/

class Solution {
    companion object {
        const val QUERY = "SELECT MIN(log_id) AS start_id, MAX(log_id) AS end_id\n" +
            "FROM (\n" +
            "    SELECT log_id, log_id - ROW_NUMBER() OVER (ORDER BY log_id) AS grp\n" +
            "    FROM Logs\n" +
            ") numbered\n" +
            "GROUP BY grp\n" +
            "ORDER BY start_id"
    }
}
