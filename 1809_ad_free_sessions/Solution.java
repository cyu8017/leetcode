// LeetCode 1809 - Ad-Free Sessions
// https://leetcode.com/problems/ad-free-sessions/

public class Solution {
    public static final String QUERY = "SELECT p.session_id\n" +
        "FROM Playback p\n" +
        "WHERE NOT EXISTS (\n" +
        "    SELECT 1\n" +
        "    FROM Ads a\n" +
        "    WHERE a.customer_id = p.customer_id\n" +
        "      AND a.timestamp BETWEEN p.start_time AND p.end_time\n" +
        ");\n" +
        "";
}
