// LeetCode 1587 - Bank Account Summary II
// https://leetcode.com/problems/bank-account-summary-ii/

const char* QUERY =
    "\n"
    "SELECT u.name, SUM(t.amount) AS balance\n"
    "FROM Users u JOIN Transactions t ON t.account = u.account\n"
    "GROUP BY u.account, u.name\n"
    "HAVING SUM(t.amount) > 10000\\n\n";
