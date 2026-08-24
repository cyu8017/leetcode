// LeetCode 1158 - Market Analysis I
// https://leetcode.com/problems/market-analysis-i/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    u.user_id AS buyer_id,\n" +
            "    u.join_date,\n" +
            "    COUNT(o.order_id) AS orders_in_2019\n" +
            "FROM Users u\n" +
            "LEFT JOIN Orders o\n" +
            "    ON u.user_id = o.buyer_id\n" +
            "   AND YEAR(o.order_date) = 2019\n" +
            "GROUP BY u.user_id, u.join_date"
    }
}
