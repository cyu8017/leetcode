// LeetCode 1867 - Orders With Maximum Quantity Above Average
// https://leetcode.com/problems/orders-with-maximum-quantity-above-average/

class Solution {
    companion object {
        const val QUERY = "        WITH OrderStats AS (\n" +
            "            SELECT\n" +
            "                order_id,\n" +
            "                MAX(quantity) AS max_qty,\n" +
            "                SUM(quantity) * 1.0 / COUNT(*) AS avg_qty\n" +
            "            FROM OrdersDetails\n" +
            "            GROUP BY order_id\n" +
            "        ),\n" +
            "        MaxAvg AS (\n" +
            "            SELECT MAX(avg_qty) AS threshold\n" +
            "            FROM OrderStats\n" +
            "        )\n" +
            "        SELECT order_id\n" +
            "        FROM OrderStats, MaxAvg\n" +
            "        WHERE max_qty > threshold\n" +
            "        "
    }
}
