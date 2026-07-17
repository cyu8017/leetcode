// LeetCode 1757 - Recyclable and Low Fat Products
// https://leetcode.com/problems/recyclable-and-low-fat-products/

class Solution {
    companion object {
        const val QUERY = "SELECT product_id\n" +
            "FROM Products\n" +
            "WHERE low_fats = 'Y' AND recyclable = 'Y';\n"
    }
}
