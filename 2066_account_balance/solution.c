// LeetCode 2066 - Account Balance
// https://leetcode.com/problems/account-balance/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    account_id,\n"
    "    day,\n"
    "    SUM(IF(type = 'Deposit', amount, -amount)) OVER (\n"
    "        PARTITION BY account_id\n"
    "        ORDER BY day\n"
    "    ) AS balance\n"
    "FROM Transactions\n"
    "ORDER BY 1, 2\n";
