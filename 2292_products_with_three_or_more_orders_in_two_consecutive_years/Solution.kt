// LeetCode 2292 - Products With Three Or More Orders In Two Consecutive Years
// https://leetcode.com/problems/products-with-three-or-more-orders-in-two-consecutive-years/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    P AS (\n" +
            "        SELECT product_id, YEAR(purchase_date) AS y, COUNT(1) >= 3 AS mark\n" +
            "        FROM Orders\n" +
            "        GROUP BY 1, 2\n" +
            "    )\n" +
            "SELECT DISTINCT p1.product_id\n" +
            "FROM\n" +
            "    P AS p1\n" +
            "    JOIN P AS p2 ON p1.y = p2.y - 1 AND p1.product_id = p2.product_id\n" +
            "WHERE p1.mark AND p2.mark"
    }
}
