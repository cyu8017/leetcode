# LeetCode 0584 - Find Customer Referee
# https:# leetcode.com/problems/find-customer-referee/

QUERY = <<~SQL
  SELECT name
  FROM Customer
  WHERE referee_id != 2 OR referee_id IS NULL
SQL
