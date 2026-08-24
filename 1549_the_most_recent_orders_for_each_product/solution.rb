# LeetCode 1549 - The Most Recent Orders For Each Product
# https://leetcode.com/problems/the-most-recent-orders-for-each-product/

QUERY = <<~SQL
  SELECT p.product_name, o.product_id, o.order_id, o.order_date
  FROM Orders o
  JOIN Products p ON p.product_id = o.product_id
  WHERE o.order_date = (
      SELECT MAX(o2.order_date) FROM Orders o2 WHERE o2.product_id = o.product_id
  )
  ORDER BY p.product_name, o.product_id, o.order_id
SQL
