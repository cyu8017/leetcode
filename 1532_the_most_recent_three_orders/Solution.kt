// LeetCode 1532 - The Most Recent Three Orders
// https://leetcode.com/problems/the-most-recent-three-orders/

class Solution {
    companion object {
        const val QUERY = "SELECT c.name AS customer_name, c.customer_id, o.order_id, o.order_date\n" +
            "FROM Customers c\n" +
            "JOIN Orders o ON o.customer_id = c.customer_id\n" +
            "WHERE (\n" +
            "    SELECT COUNT(*)\n" +
            "    FROM Orders o2\n" +
            "    WHERE o2.customer_id = o.customer_id\n" +
            "      AND (o2.order_date > o.order_date OR (o2.order_date = o.order_date AND o2.order_id > o.order_id))\n" +
            ") < 3\n" +
            "ORDER BY c.name, c.customer_id, o.order_date DESC"
    }
}
