# LeetCode 2066 - Account Balance
# https:# leetcode.com/problems/account-balance/

QUERY = <<~SQL
  SELECT
      account_id,
      day,
      SUM(IF(type = 'Deposit', amount, -amount)) OVER (
          PARTITION BY account_id
          ORDER BY day
      ) AS balance
  FROM Transactions
  ORDER BY 1, 2
SQL
