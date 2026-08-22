// LeetCode 1336 - Number of Transactions per Visit
// https://leetcode.com/problems/number-of-transactions-per-visit/

const char* QUERY =
    "\n"
    "WITH RECURSIVE counts AS (\n"
    "    SELECT 0 AS transactions_count\n"
    "    UNION ALL\n"
    "    SELECT transactions_count + 1\n"
    "    FROM counts\n"
    "    WHERE transactions_count < (SELECT COUNT(*) FROM Transactions GROUP BY user_id, transaction_date ORDER BY COUNT(*) DESC LIMIT 1)\n"
    "), per_visit AS (\n"
    "    SELECT v.user_id, v.visit_date, COUNT(t.amount) AS transactions_count\n"
    "    FROM Visits v\n"
    "    LEFT JOIN Transactions t\n"
    "      ON t.user_id = v.user_id AND t.transaction_date = v.visit_date\n"
    "    GROUP BY v.user_id, v.visit_date\n"
    ")\n"
    "SELECT c.transactions_count, COUNT(p.transactions_count) AS visits_count\n"
    "FROM counts c\n"
    "LEFT JOIN per_visit p USING (transactions_count)\n"
    "GROUP BY c.transactions_count\n"
    "ORDER BY c.transactions_count\n";
