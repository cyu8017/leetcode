// LeetCode 1783 - Grand Slam Titles
// https://leetcode.com/problems/grand-slam-titles/

public class Solution
{
    public const string QUERY = "SELECT p.player_id, p.player_name, COUNT(*) AS grand_slams_count\n" +
        "FROM Players p\n" +
        "JOIN (\n" +
        "    SELECT Wimbledon AS player_id FROM Championships\n" +
        "    UNION ALL SELECT Fr_open FROM Championships\n" +
        "    UNION ALL SELECT US_open FROM Championships\n" +
        "    UNION ALL SELECT Au_open FROM Championships\n" +
        ") w ON p.player_id = w.player_id\n" +
        "GROUP BY p.player_id, p.player_name;\n" +
        "";
}
