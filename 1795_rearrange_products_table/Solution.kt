// LeetCode 1795 - Rearrange Products Table
// https://leetcode.com/problems/rearrange-products-table/

class Solution {
    companion object {
        const val QUERY = "SELECT product_id, 'store1' AS store, store1 AS price FROM Products WHERE store1 IS NOT NULL\n" +
            "UNION ALL\n" +
            "SELECT product_id, 'store2', store2 FROM Products WHERE store2 IS NOT NULL\n" +
            "UNION ALL\n" +
            "SELECT product_id, 'store3', store3 FROM Products WHERE store3 IS NOT NULL;\n" +
            ""
    }
}
