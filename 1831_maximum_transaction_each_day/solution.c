// LeetCode 1831 - Maximum Transaction Each Day
// https://leetcode.com/problems/maximum-transaction-each-day/

const char* QUERY =
    "\n"
    "SELECT transaction_id\n"
    "FROM Transactions t\n"
    "WHERE amount = (\n"
    "    SELECT MAX(amount)\n"
    "    FROM Transactions\n"
    "    WHERE DATE(day) = DATE(t.day)\n"
    ")\n"
    "ORDER BY transaction_id\n";
