// LeetCode 3521 - Find Product Recommendation Pairs
// https://leetcode.com/problems/find-product-recommendation-pairs/

class Solution {
    companion object {
        const val QUERY = "WITH purchase_info_cte AS (\n" +
            "    SELECT p.user_id, p.product_id, i.category\n" +
            "    FROM ProductPurchases p INNER JOIN ProductInfo i ON p.product_id = i.product_id\n" +
            ")\n" +
            "\n" +
            "SELECT a.product_id AS product1_id,\n" +
            "       b.product_id AS product2_id,\n" +
            "       a.category AS product1_category,\n" +
            "       b.category AS product2_category,\n" +
            "       COUNT(*) AS customer_count\n" +
            "FROM purchase_info_cte a\n" +
            "INNER JOIN purchase_info_cte b ON a.user_id = b.user_id AND a.product_id < b.product_id\n" +
            "GROUP BY 1, 2\n" +
            "HAVING COUNT(*) >= 3\n" +
            "ORDER BY 5 DESC, 1, 2;"
    }
}
