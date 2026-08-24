// LeetCode 2922 - Market Analysis Iii
// https://leetcode.com/problems/market-analysis-iii/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT seller_id, COUNT(DISTINCT item_id) AS num_items\n" +
            "        FROM\n" +
            "            Orders\n" +
            "            JOIN Users USING (seller_id)\n" +
            "            JOIN Items USING (item_id)\n" +
            "        WHERE item_brand != favorite_brand\n" +
            "        GROUP BY 1\n" +
            "    )\n" +
            "SELECT seller_id, num_items\n" +
            "FROM T\n" +
            "WHERE num_items = (SELECT MAX(num_items) FROM T)\n" +
            "ORDER BY 1"
    }
}
