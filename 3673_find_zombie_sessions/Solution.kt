// LeetCode 3673 - Find Zombie Sessions
// https://leetcode.com/problems/find-zombie-sessions/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    session_id,\n" +
            "    user_id,\n" +
            "    TIMESTAMPDIFF(MINUTE, MIN(event_timestamp), MAX(event_timestamp)) session_duration_minutes,\n" +
            "    SUM(event_type = 'scroll') scroll_count\n" +
            "FROM app_events\n" +
            "GROUP BY session_id\n" +
            "HAVING\n" +
            "    session_duration_minutes >= 30\n" +
            "    AND SUM(event_type = 'click') / SUM(event_type = 'scroll') < 0.2\n" +
            "    AND SUM(event_type = 'purchase') = 0\n" +
            "    AND SUM(event_type = 'scroll') >= 5\n" +
            "ORDER BY scroll_count DESC, session_id;"
    }
}
