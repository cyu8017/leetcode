# LeetCode 1677 - Products Worth Over Invoices
# https://leetcode.com/problems/products-worth-over-invoices/

QUERY = <<~SQL
  SELECT p.name, COALESCE(SUM(i.rest),0) rest, COALESCE(SUM(i.paid),0) paid,
  COALESCE(SUM(i.canceled),0) canceled, COALESCE(SUM(i.refunded),0) refunded
  FROM Product p LEFT JOIN Invoice i USING(product_id) GROUP BY p.product_id, p.name ORDER BY p.name
SQL
