// LeetCode 2159 - Order Two Columns Independently
// https://leetcode.com/problems/order-two-columns-independently/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    S AS (\n" +
            "        SELECT\n" +
            "            first_col,\n" +
            "            ROW_NUMBER() OVER (ORDER BY first_col) AS rk\n" +
            "        FROM Data\n" +
            "    ),\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            second_col,\n" +
            "            ROW_NUMBER() OVER (ORDER BY second_col DESC) AS rk\n" +
            "        FROM Data\n" +
            "    )\n" +
            "SELECT first_col, second_col\n" +
            "FROM\n" +
            "    S\n" +
            "    JOIN T USING (rk)"
    }
}
