// LeetCode 2994 - Friday Purchases Ii
// https://leetcode.com/problems/friday-purchases-ii/

class Solution {
    companion object {
        const val QUERY = "WITH RECURSIVE\n" +
            "    T AS (\n" +
            "        SELECT '2023-11-01' AS purchase_date\n" +
            "        UNION\n" +
            "        SELECT purchase_date + INTERVAL 1 DAY\n" +
            "        FROM T\n" +
            "        WHERE purchase_date < '2023-11-30'\n" +
            "    )\n" +
            "SELECT\n" +
            "    CEIL(DAYOFMONTH(purchase_date) / 7) AS week_of_month,\n" +
            "    purchase_date,\n" +
            "    IFNULL(SUM(amount_spend), 0) AS total_amount\n" +
            "FROM\n" +
            "    T\n" +
            "    LEFT JOIN Purchases USING (purchase_date)\n" +
            "WHERE DAYOFWEEK(purchase_date) = 6\n" +
            "GROUP BY 2\n" +
            "ORDER BY 1"
    }
}
