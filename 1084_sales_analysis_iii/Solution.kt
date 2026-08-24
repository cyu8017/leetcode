// LeetCode 1084 - Sales Analysis Iii
// https://leetcode.com/problems/sales-analysis-iii/

class Solution {
    companion object {
        const val QUERY = "SELECT DISTINCT p.product_id, p.product_name\n" +
            "FROM Product p\n" +
            "JOIN Sales s ON p.product_id = s.product_id\n" +
            "GROUP BY p.product_id, p.product_name\n" +
            "HAVING MIN(s.sale_date) >= '2019-01-01'\n" +
            "   AND MAX(s.sale_date) <= '2019-03-31'"
    }
}
