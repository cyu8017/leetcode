// LeetCode 1327 - List The Products Ordered In A Period
// https://leetcode.com/problems/list-the-products-ordered-in-a-period/

class Solution {
    companion object {
        const val QUERY = "SELECT p.product_name, SUM(o.unit) AS unit\n" +
            "FROM Products p\n" +
            "JOIN Orders o USING (product_id)\n" +
            "WHERE o.order_date >= '2020-02-01' AND o.order_date < '2020-03-01'\n" +
            "GROUP BY p.product_id, p.product_name\n" +
            "HAVING SUM(o.unit) >= 100"
    }
}
