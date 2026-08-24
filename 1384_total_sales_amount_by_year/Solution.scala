// LeetCode 1384 - Total Sales Amount By Year
// https://leetcode.com/problems/total-sales-amount-by-year/

object Solution {
  final val QUERY: String = """SELECT p.product_name, s.year,
       (DATEDIFF(LEAST(s.period_end, CONCAT(s.year, '-12-31')),
                 GREATEST(s.period_start, CONCAT(s.year, '-01-01'))) + 1)
       * p.average_daily_sales AS total_amount
FROM Product p
JOIN (
  SELECT product_id, period_start, period_end, average_daily_sales, 2018 year FROM Sales
  UNION ALL SELECT product_id, period_start, period_end, average_daily_sales, 2019 FROM Sales
  UNION ALL SELECT product_id, period_start, period_end, average_daily_sales, 2020 FROM Sales
) s ON p.product_id=s.product_id
WHERE s.period_start <= CONCAT(s.year,'-12-31') AND s.period_end >= CONCAT(s.year,'-01-01')
ORDER BY p.product_id, s.year
"""
}
