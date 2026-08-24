// LeetCode 1321 - Restaurant Growth
// https://leetcode.com/problems/restaurant-growth/

class Solution {
    companion object {
        const val QUERY = "WITH daily AS (\n" +
            "    SELECT visited_on, SUM(amount) AS amount\n" +
            "    FROM Customer\n" +
            "    GROUP BY visited_on\n" +
            ")\n" +
            "SELECT visited_on,\n" +
            "       SUM(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount,\n" +
            "       ROUND(AVG(amount) OVER (ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) AS average_amount\n" +
            "FROM daily\n" +
            "ORDER BY visited_on\n" +
            "LIMIT 18446744073709551615 OFFSET 6"
    }
}
