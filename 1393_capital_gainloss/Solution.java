// LeetCode 1393 - Capital Gain/Loss
// https://leetcode.com/problems/capital-gainloss/

class Solution {
    public static final String QUERY = """
SELECT stock_name,
       SUM(CASE WHEN operation = 'Sell' THEN price ELSE -price END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name
""";
}
