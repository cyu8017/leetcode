// LeetCode 2720 - Popularity Percentage
// https://leetcode.com/problems/popularity-percentage/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    F AS (\n" +
            "        SELECT * FROM Friends\n" +
            "        UNION\n" +
            "        SELECT user2, user1 FROM Friends\n" +
            "    ),\n" +
            "    T AS (SELECT COUNT(DISTINCT user1) AS cnt FROM F)\n" +
            "SELECT DISTINCT\n" +
            "    user1,\n" +
            "    ROUND(\n" +
            "        (COUNT(1) OVER (PARTITION BY user1)) * 100 / (SELECT cnt FROM T),\n" +
            "        2\n" +
            "    ) AS percentage_popularity\n" +
            "FROM F\n" +
            "ORDER BY 1"
    }
}
