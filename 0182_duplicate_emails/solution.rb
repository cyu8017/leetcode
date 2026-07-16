# LeetCode 0182 - Duplicate Emails
# https://leetcode.com/problems/duplicate-emails/

QUERY = <<~SQL
  SELECT email AS Email
  FROM Person
  GROUP BY email
  HAVING COUNT(*) > 1
SQL