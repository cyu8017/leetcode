// LeetCode 3497 - Analyze Subscription Conversion
// https://leetcode.com/problems/analyze-subscription-conversion/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT user_id, activity_type, ROUND(SUM(activity_duration) / COUNT(1), 2) duration\n" +
            "        FROM UserActivity\n" +
            "        WHERE activity_type != 'cancelled'\n" +
            "        GROUP BY user_id, activity_type\n" +
            "    ),\n" +
            "    F AS (\n" +
            "        SELECT user_id, duration trial_avg_duration\n" +
            "        FROM T\n" +
            "        WHERE activity_type = 'free_trial'\n" +
            "    ),\n" +
            "    P AS (\n" +
            "        SELECT user_id, duration paid_avg_duration\n" +
            "        FROM T\n" +
            "        WHERE activity_type = 'paid'\n" +
            "    )\n" +
            "SELECT user_id, trial_avg_duration, paid_avg_duration\n" +
            "FROM\n" +
            "    F\n" +
            "    JOIN P USING (user_id)\n" +
            "ORDER BY 1;"
    }
}
