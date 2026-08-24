// LeetCode 1068 - Product Sales Analysis I
// https://leetcode.com/problems/product-sales-analysis-i/

class Solution {
    companion object {
        const val QUERY = "SELECT p.product_name, s.year, s.price\n" +
            "FROM Sales s\n" +
            "JOIN Product p ON s.product_id = p.product_id"
    }
}
