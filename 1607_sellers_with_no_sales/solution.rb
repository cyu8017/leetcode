# LeetCode 1607 - Sellers With No Sales
# https://leetcode.com/problems/sellers-with-no-sales/

QUERY = <<~SQL
  SELECT seller_name
  FROM Seller
  WHERE seller_id NOT IN (
      SELECT seller_id FROM Orders
      WHERE sale_date BETWEEN '2020-01-01' AND '2020-12-31'
  )
  ORDER BY seller_name;
SQL
