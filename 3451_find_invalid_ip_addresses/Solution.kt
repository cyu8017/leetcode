// LeetCode 3451 - Find Invalid Ip Addresses
// https://leetcode.com/problems/find-invalid-ip-addresses/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    ip,\n" +
            "    COUNT(*) AS invalid_count\n" +
            "FROM logs\n" +
            "WHERE\n" +
            "    LENGTH(ip) - LENGTH(REPLACE(ip, '.', '')) != 3\n" +
            "\n" +
            "    OR SUBSTRING_INDEX(ip, '.', 1) REGEXP '^0[0-9]'\n" +
            "    OR SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1) REGEXP '^0[0-9]'\n" +
            "    OR SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1) REGEXP '^0[0-9]'\n" +
            "    OR SUBSTRING_INDEX(ip, '.', -1) REGEXP '^0[0-9]'\n" +
            "\n" +
            "    OR SUBSTRING_INDEX(ip, '.', 1) > 255\n" +
            "    OR SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 2), '.', -1) > 255\n" +
            "    OR SUBSTRING_INDEX(SUBSTRING_INDEX(ip, '.', 3), '.', -1) > 255\n" +
            "    OR SUBSTRING_INDEX(ip, '.', -1) > 255\n" +
            "\n" +
            "GROUP BY 1\n" +
            "ORDER BY 2 DESC, 1 DESC;"
    }
}
