// LeetCode 1083 - Sales Analysis Ii
// https://leetcode.com/problems/sales-analysis-ii/

class Solution {
    companion object {
        const val QUERY = "SELECT DISTINCT s.buyer_id\n" +
            "FROM Sales s\n" +
            "JOIN Product p ON s.product_id = p.product_id\n" +
            "WHERE p.product_name = 'S8'\n" +
            "  AND s.buyer_id NOT IN (\n" +
            "      SELECT s2.buyer_id\n" +
            "      FROM Sales s2\n" +
            "      JOIN Product p2 ON s2.product_id = p2.product_id\n" +
            "      WHERE p2.product_name = 'iPhone'\n" +
            "  )"
    }
}
