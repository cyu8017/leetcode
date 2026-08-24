// LeetCode 3124 - Find Longest Calls
// https://leetcode.com/problems/find-longest-calls/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            first_name,\n" +
            "            type,\n" +
            "            DATE_FORMAT(SEC_TO_TIME(duration), \"%H:%i:%s\") AS duration_formatted,\n" +
            "            RANK() OVER (\n" +
            "                PARTITION BY type\n" +
            "                ORDER BY duration DESC\n" +
            "            ) AS rk\n" +
            "        FROM\n" +
            "            Calls AS c1\n" +
            "            JOIN Contacts AS c2 ON c1.contact_id = c2.id\n" +
            "    )\n" +
            "SELECT\n" +
            "    first_name,\n" +
            "    type,\n" +
            "    duration_formatted\n" +
            "FROM T\n" +
            "WHERE rk <= 3\n" +
            "ORDER BY 2, 3 DESC, 1 DESC;"
    }
}
