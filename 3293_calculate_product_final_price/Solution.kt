// LeetCode 3293 - Calculate Product Final Price
// https://leetcode.com/problems/calculate-product-final-price/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    product_id,\n" +
            "    price * (100 - IFNULL(discount, 0)) / 100 final_price,\n" +
            "    category\n" +
            "FROM\n" +
            "    Products\n" +
            "    LEFT JOIN Discounts USING (category)\n" +
            "ORDER BY 1;"
    }
}
