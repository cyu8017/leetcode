# LeetCode 1511 - Customer Order Frequency
# https://leetcode.com/problems/customer-order-frequency/

QUERY = <<~SQL
  SELECT c.customer_id, c.name
  FROM Customers c
  JOIN Orders o ON o.customer_id = c.customer_id
  JOIN Product p ON p.product_id = o.product_id
  GROUP BY c.customer_id, c.name
  HAVING SUM(CASE WHEN LEFT(o.order_date, 7) = '2020-06' THEN o.quantity * p.price ELSE 0 END) >= 100
     AND SUM(CASE WHEN LEFT(o.order_date, 7) = '2020-07' THEN o.quantity * p.price ELSE 0 END) >= 100
SQL
