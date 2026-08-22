// LeetCode 1393 - Capital Gain/Loss
// https://leetcode.com/problems/capital-gainloss/

const char* QUERY =
    "\n"
    "SELECT stock_name,\n"
    "       SUM(CASE WHEN operation = 'Sell' THEN price ELSE -price END) AS capital_gain_loss\n"
    "FROM Stocks\n"
    "GROUP BY stock_name\n";
