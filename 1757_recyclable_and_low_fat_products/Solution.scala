// LeetCode 1757 - Recyclable and Low Fat Products
// https://leetcode.com/problems/recyclable-and-low-fat-products/

object Solution {
  final val QUERY: String = """SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
"""
}
