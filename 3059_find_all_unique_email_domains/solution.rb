# LeetCode 3059 - Find All Unique Email Domains
# https:# leetcode.com/problems/find-all-unique-email-domains/

QUERY = <<~SQL
  SELECT SUBSTRING_INDEX(email, '@', -1) AS email_domain, COUNT(1) AS count
  FROM Emails
  WHERE email LIKE '%.com'
  GROUP BY 1
  ORDER BY 1;
SQL
