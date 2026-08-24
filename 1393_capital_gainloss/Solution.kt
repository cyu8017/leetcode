// LeetCode 1393 - Capital Gainloss
// https://leetcode.com/problems/capital-gainloss/

class Solution {
    companion object {
        const val QUERY = "SELECT stock_name,\n" +
            "       SUM(CASE WHEN operation = 'Sell' THEN price ELSE -price END) AS capital_gain_loss\n" +
            "FROM Stocks\n" +
            "GROUP BY stock_name"
    }
}
