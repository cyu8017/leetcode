// LeetCode 3554 - Find Category Recommendation Pairs
// https://leetcode.com/problems/find-category-recommendation-pairs/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    user_category AS (\n" +
            "        SELECT DISTINCT\n" +
            "            user_id,\n" +
            "            category\n" +
            "        FROM\n" +
            "            ProductPurchases\n" +
            "            JOIN ProductInfo USING (product_id)\n" +
            "    ),\n" +
            "    pair_per_user AS (\n" +
            "        SELECT\n" +
            "            a.user_id,\n" +
            "            a.category AS category1,\n" +
            "            b.category AS category2\n" +
            "        FROM\n" +
            "            user_category AS a\n" +
            "            JOIN user_category AS b ON a.user_id = b.user_id AND a.category < b.category\n" +
            "    )\n" +
            "SELECT category1, category2, COUNT(DISTINCT user_id) AS customer_count\n" +
            "FROM pair_per_user\n" +
            "GROUP BY 1, 2\n" +
            "HAVING customer_count >= 3\n" +
            "ORDER BY 3 DESC, 1, 2;"
    }
}
