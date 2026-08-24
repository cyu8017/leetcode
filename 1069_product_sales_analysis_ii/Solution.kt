// LeetCode 1069 - Product Sales Analysis Ii
// https://leetcode.com/problems/product-sales-analysis-ii/

class Solution {
    companion object {
        const val QUERY = "SELECT product_id, SUM(quantity) AS total_quantity\n" +
            "FROM Sales\n" +
            "GROUP BY product_id"
    }
}
