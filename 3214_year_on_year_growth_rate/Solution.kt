// LeetCode 3214 - Year On Year Growth Rate
// https://leetcode.com/problems/year-on-year-growth-rate/

class Solution {
    companion object {
        const val QUERY = "WITH\n" +
            "    T AS (\n" +
            "        SELECT product_id, YEAR(transaction_date) year, SUM(spend) curr_year_spend\n" +
            "        FROM user_transactions\n" +
            "        GROUP BY 1, 2\n" +
            "    ),\n" +
            "    S AS (\n" +
            "        SELECT t1.year, t1.product_id, t1.curr_year_spend, t2.curr_year_spend prev_year_spend\n" +
            "        FROM\n" +
            "            T t1\n" +
            "            LEFT JOIN T t2 ON t1.product_id = t2.product_id AND t1.year = t2.year + 1\n" +
            "    )\n" +
            "SELECT\n" +
            "    *,\n" +
            "    ROUND((curr_year_spend - prev_year_spend) / prev_year_spend * 100, 2) yoy_rate\n" +
            "FROM S\n" +
            "ORDER BY 2, 1;"
    }
}
