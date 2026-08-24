// LeetCode 1069 - Product Sales Analysis II
// https://leetcode.com/problems/product-sales-analysis-ii/

object Solution {
  final val QUERY: String = """SELECT product_id, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY product_id
"""
}
