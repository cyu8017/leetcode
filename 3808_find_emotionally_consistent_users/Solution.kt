// LeetCode 3808 - Find Emotionally Consistent Users
// https://leetcode.com/problems/find-emotionally-consistent-users/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    t AS (\n" +
            "        SELECT\n" +
            "            user_id,\n" +
            "            reaction,\n" +
            "            COUNT(1) cnt\n" +
            "        FROM reactions\n" +
            "        GROUP BY 1, 2\n" +
            "    ),\n" +
            "    s AS (\n" +
            "        SELECT\n" +
            "            user_id,\n" +
            "            MAX(cnt) mx_cnt,\n" +
            "            ROUND(MAX(cnt) / SUM(cnt), 2) reaction_ratio\n" +
            "        FROM t\n" +
            "        GROUP BY 1\n" +
            "        HAVING reaction_ratio >= 0.60 AND SUM(cnt) >= 5\n" +
            "    )\n" +
            "SELECT user_id, reaction dominant_reaction, reaction_ratio\n" +
            "FROM\n" +
            "    s\n" +
            "    JOIN t USING (user_id)\n" +
            "WHERE cnt = mx_cnt\n" +
            "ORDER BY 3 DESC, 1;"
    }
}
