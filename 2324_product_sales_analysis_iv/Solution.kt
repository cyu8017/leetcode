// LeetCode 2324 - Product Sales Analysis Iv
// https://leetcode.com/problems/product-sales-analysis-iv/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            user_id,\n" +
            "            product_id,\n" +
            "            RANK() OVER (\n" +
            "                PARTITION BY user_id\n" +
            "                ORDER BY SUM(quantity * price) DESC\n" +
            "            ) AS rk\n" +
            "        FROM\n" +
            "            Sales\n" +
            "            JOIN Product USING (product_id)\n" +
            "        GROUP BY 1, 2\n" +
            "    )\n" +
            "SELECT user_id, product_id\n" +
            "FROM T\n" +
            "WHERE rk = 1"
    }
}
