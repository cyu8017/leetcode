// LeetCode 2701 - Consecutive Transactions With Increasing Amounts
// https://leetcode.com/problems/consecutive-transactions-with-increasing-amounts/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT\n" +
            "            t1.*,\n" +
            "            SUM(\n" +
            "                CASE\n" +
            "                    WHEN t2.customer_id IS NULL THEN 1\n" +
            "                    ELSE 0\n" +
            "                END\n" +
            "            ) OVER (ORDER BY customer_id, transaction_date) AS s\n" +
            "        FROM\n" +
            "            Transactions AS t1\n" +
            "            LEFT JOIN Transactions AS t2\n" +
            "                ON t1.customer_id = t2.customer_id\n" +
            "                AND t1.amount > t2.amount\n" +
            "                AND DATEDIFF(t1.transaction_date, t2.transaction_date) = 1\n" +
            "    )\n" +
            "SELECT\n" +
            "    customer_id,\n" +
            "    MIN(transaction_date) AS consecutive_start,\n" +
            "    MAX(transaction_date) AS consecutive_end\n" +
            "FROM T\n" +
            "GROUP BY customer_id, s\n" +
            "HAVING COUNT(1) >= 3\n" +
            "ORDER BY customer_id"
    }
}
