// LeetCode 2985 - Calculate Compressed Mean
// https://leetcode.com/problems/calculate-compressed-mean/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    ROUND(\n" +
            "        SUM(item_count * order_occurrences) / SUM(order_occurrences),\n" +
            "        2\n" +
            "    ) AS average_items_per_order\n" +
            "FROM Orders"
    }
}
