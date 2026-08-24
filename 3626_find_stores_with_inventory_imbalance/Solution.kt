// LeetCode 3626 - Find Stores With Inventory Imbalance
// https://leetcode.com/problems/find-stores-with-inventory-imbalance/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            store_id,\n" +
            "            product_name,\n" +
            "            quantity,\n" +
            "            RANK() OVER (\n" +
            "                PARTITION BY store_id\n" +
            "                ORDER BY price DESC, quantity DESC\n" +
            "            ) rk1,\n" +
            "            RANK() OVER (\n" +
            "                PARTITION BY store_id\n" +
            "                ORDER BY price, quantity DESC\n" +
            "            ) rk2,\n" +
            "            COUNT(1) OVER (PARTITION BY store_id) cnt\n" +
            "        FROM inventory\n" +
            "    ),\n" +
            "    P1 AS (\n" +
            "        SELECT *\n" +
            "        FROM T\n" +
            "        WHERE rk1 = 1 AND cnt >= 3\n" +
            "    ),\n" +
            "    P2 AS (\n" +
            "        SELECT *\n" +
            "        FROM T\n" +
            "        WHERE rk2 = 1\n" +
            "    )\n" +
            "SELECT\n" +
            "    s.store_id store_id,\n" +
            "    store_name,\n" +
            "    location,\n" +
            "    p1.product_name most_exp_product,\n" +
            "    p2.product_name cheapest_product,\n" +
            "    ROUND(p2.quantity / p1.quantity, 2) imbalance_ratio\n" +
            "FROM\n" +
            "    P1 p1\n" +
            "    JOIN P2 p2 ON p1.store_id = p2.store_id AND p1.quantity < p2.quantity\n" +
            "    JOIN stores s ON p1.store_id = s.store_id\n" +
            "ORDER BY imbalance_ratio DESC, store_name;"
    }
}
