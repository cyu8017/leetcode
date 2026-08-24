# LeetCode 2082 - The Number of Rich Customers
# https:# leetcode.com/problems/the-number-of-rich-customers/

QUERY = <<~SQL
  SELECT
      COUNT(DISTINCT customer_id) AS rich_count
  FROM Store
  WHERE amount > 500
SQL
