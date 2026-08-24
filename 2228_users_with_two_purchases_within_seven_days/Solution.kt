// LeetCode 2228 - Users With Two Purchases Within Seven Days
// https://leetcode.com/problems/users-with-two-purchases-within-seven-days/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    t AS (\n" +
            "        SELECT\n" +
            "            user_id,\n" +
            "            DATEDIFF(\n" +
            "                purchase_date,\n" +
            "                LAG(purchase_date, 1) OVER (\n" +
            "                    PARTITION BY user_id\n" +
            "                    ORDER BY purchase_date\n" +
            "                )\n" +
            "            ) AS d\n" +
            "        FROM Purchases\n" +
            "    )\n" +
            "SELECT DISTINCT user_id\n" +
            "FROM t\n" +
            "WHERE d <= 7\n" +
            "ORDER BY user_id"
    }
}
