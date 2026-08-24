// LeetCode 2688 - Find Active Users
// https://leetcode.com/problems/find-active-users/

class Solution {
    companion object {
        const val QUERY = "SELECT DISTINCT\n" +
            "    user_id\n" +
            "FROM Users\n" +
            "WHERE\n" +
            "    user_id IN (\n" +
            "        SELECT\n" +
            "            user_id\n" +
            "        FROM\n" +
            "            (\n" +
            "                SELECT\n" +
            "                    user_id,\n" +
            "                    created_at,\n" +
            "                    LAG(created_at, 1) OVER (\n" +
            "                        PARTITION BY user_id\n" +
            "                        ORDER BY created_at\n" +
            "                    ) AS prev_created_at\n" +
            "                FROM Users\n" +
            "            ) AS t\n" +
            "        WHERE DATEDIFF(created_at, prev_created_at) <= 7\n" +
            "    )"
    }
}
