// LeetCode 3220 - Odd and Even Transactions
// https://leetcode.com/problems/odd-and-even-transactions/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    transaction_date,\n"
    "    SUM(IF(amount % 2 = 1, amount, 0)) AS odd_sum,\n"
    "    SUM(IF(amount % 2 = 0, amount, 0)) AS even_sum\n"
    "FROM transactions\n"
    "GROUP BY 1\n"
    "ORDER BY 1;\n";
