// LeetCode 1070 - Product Sales Analysis Iii
// https://leetcode.com/problems/product-sales-analysis-iii/

class Solution {
    companion object {
        const val QUERY = "SELECT product_id, year AS first_year, quantity, price\n" +
            "FROM Sales\n" +
            "WHERE (product_id, year) IN (\n" +
            "    SELECT product_id, MIN(year)\n" +
            "    FROM Sales\n" +
            "    GROUP BY product_id\n" +
            ")"
    }
}
