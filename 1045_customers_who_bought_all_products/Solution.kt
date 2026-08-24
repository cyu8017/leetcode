// LeetCode 1045 - Customers Who Bought All Products
// https://leetcode.com/problems/customers-who-bought-all-products/

class Solution {
    companion object {
        const val QUERY = "SELECT customer_id\n" +
            "FROM Customer\n" +
            "GROUP BY customer_id\n" +
            "HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)"
    }
}
