// LeetCode 1777 - Product's Price for Each Store
// https://leetcode.com/problems/products-price-for-each-store/

class Solution {
    companion object {
        const val QUERY = "SELECT product_id,\n" +
            "       MAX(CASE WHEN store = 'store1' THEN price END) AS store1,\n" +
            "       MAX(CASE WHEN store = 'store2' THEN price END) AS store2,\n" +
            "       MAX(CASE WHEN store = 'store3' THEN price END) AS store3\n" +
            "FROM Products\n" +
            "GROUP BY product_id;\n" +
            ""
    }
}
