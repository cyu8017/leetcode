// LeetCode 3089 - Find Bursty Behavior
// https://leetcode.com/problems/find-bursty-behavior/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    P AS (\n" +
            "        SELECT p1.user_id AS user_id, COUNT(1) AS cnt\n" +
            "        FROM\n" +
            "            Posts AS p1\n" +
            "            JOIN Posts AS p2\n" +
            "                ON p1.user_id = p2.user_id\n" +
            "                AND p2.post_date BETWEEN p1.post_date AND DATE_ADD(p1.post_date, INTERVAL 6 DAY)\n" +
            "        GROUP BY p1.user_id, p1.post_id\n" +
            "    ),\n" +
            "    T AS (\n" +
            "        SELECT user_id, COUNT(1) / 4 AS avg_weekly_posts\n" +
            "        FROM Posts\n" +
            "        WHERE post_date BETWEEN '2024-02-01' AND '2024-02-28'\n" +
            "        GROUP BY 1\n" +
            "    )\n" +
            "SELECT user_id, MAX(cnt) AS max_7day_posts, avg_weekly_posts\n" +
            "FROM\n" +
            "    P\n" +
            "    JOIN T USING (user_id)\n" +
            "GROUP BY 1\n" +
            "HAVING max_7day_posts >= avg_weekly_posts * 2\n" +
            "ORDER BY 1;"
    }
}
