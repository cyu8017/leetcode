# LeetCode 1393 - Capital Gainloss
# https://leetcode.com/problems/capital-gainloss/

QUERY = <<~SQL
  SELECT stock_name,
         SUM(CASE WHEN operation = 'Sell' THEN price ELSE -price END) AS capital_gain_loss
  FROM Stocks
  GROUP BY stock_name
SQL
