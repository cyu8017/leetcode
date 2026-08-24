// LeetCode 1972 - First And Last Call On The Same Day
// https://leetcode.com/problems/first-and-last-call-on-the-same-day/

class Solution {
    companion object {
        const val QUERY = "WITH s AS (\n" +
            "    SELECT caller_id, recipient_id, call_time FROM Calls\n" +
            "    UNION ALL\n" +
            "    SELECT recipient_id, caller_id, call_time FROM Calls\n" +
            "),\n" +
            "t AS (\n" +
            "    SELECT\n" +
            "        caller_id AS user_id,\n" +
            "        FIRST_VALUE(recipient_id) OVER (\n" +
            "            PARTITION BY DATE(call_time), caller_id\n" +
            "            ORDER BY call_time ASC\n" +
            "        ) AS first_peer,\n" +
            "        FIRST_VALUE(recipient_id) OVER (\n" +
            "            PARTITION BY DATE(call_time), caller_id\n" +
            "            ORDER BY call_time DESC\n" +
            "        ) AS last_peer\n" +
            "    FROM s\n" +
            ")\n" +
            "SELECT DISTINCT user_id\n" +
            "FROM t\n" +
            "WHERE first_peer = last_peer"
    }
}
