// LeetCode 3056 - Snaps Analysis
// https://leetcode.com/problems/snaps-analysis/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    age_bucket,\n" +
            "    ROUND(100 * SUM(IF(activity_type = 'send', time_spent, 0)) / SUM(time_spent), 2) AS send_perc,\n" +
            "    ROUND(100 * SUM(IF(activity_type = 'open', time_spent, 0)) / SUM(time_spent), 2) AS open_perc\n" +
            "FROM\n" +
            "    Activities\n" +
            "    JOIN Age USING (user_id)\n" +
            "GROUP BY 1;"
    }
}
