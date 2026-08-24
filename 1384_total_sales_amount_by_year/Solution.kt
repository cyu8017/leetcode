// LeetCode 1384 - Total Sales Amount By Year
// https://leetcode.com/problems/total-sales-amount-by-year/

class Solution {
    companion object {
        const val QUERY = "SELECT p.product_name, s.year,\n" +
            "       (DATEDIFF(LEAST(s.period_end, CONCAT(s.year, '-12-31')),\n" +
            "                 GREATEST(s.period_start, CONCAT(s.year, '-01-01'))) + 1)\n" +
            "       * p.average_daily_sales AS total_amount\n" +
            "FROM Product p\n" +
            "JOIN (\n" +
            "  SELECT product_id, period_start, period_end, average_daily_sales, 2018 year FROM Sales\n" +
            "  UNION ALL SELECT product_id, period_start, period_end, average_daily_sales, 2019 FROM Sales\n" +
            "  UNION ALL SELECT product_id, period_start, period_end, average_daily_sales, 2020 FROM Sales\n" +
            ") s ON p.product_id=s.product_id\n" +
            "WHERE s.period_start <= CONCAT(s.year,'-12-31') AND s.period_end >= CONCAT(s.year,'-01-01')\n" +
            "ORDER BY p.product_id, s.year"
    }
}
