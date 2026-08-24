// LeetCode 1549 - The Most Recent Orders For Each Product
// https://leetcode.com/problems/the-most-recent-orders-for-each-product/

class Solution {
    companion object {
        const val QUERY = "SELECT p.product_name, o.product_id, o.order_id, o.order_date\n" +
            "FROM Orders o\n" +
            "JOIN Products p ON p.product_id = o.product_id\n" +
            "WHERE o.order_date = (\n" +
            "    SELECT MAX(o2.order_date) FROM Orders o2 WHERE o2.product_id = o.product_id\n" +
            ")\n" +
            "ORDER BY p.product_name, o.product_id, o.order_id"
    }
}
