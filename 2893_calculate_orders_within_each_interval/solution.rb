# LeetCode 2893 - Calculate Orders Within Each Interval
# https:# leetcode.com/problems/calculate-orders-within-each-interval/

QUERY = <<~SQL
  WITH T AS (
      SELECT
          minute,
          SUM(order_count) OVER (
              ORDER BY minute
              ROWS 5 PRECEDING
          ) AS total_orders
      FROM Orders
  )
  SELECT minute DIV 6 AS interval_no, total_orders
  FROM T
  WHERE minute % 6 = 0
SQL
