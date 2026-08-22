// LeetCode 1205 - Monthly Transactions II
// https://leetcode.com/problems/monthly-transactions-ii/

const char* QUERY =
    "\n"
    "WITH activity AS (\n"
    "    SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month, country,\n"
    "           1 AS approved_count, amount AS approved_amount,\n"
    "           0 AS chargeback_count, 0 AS chargeback_amount\n"
    "    FROM Transactions\n"
    "    WHERE state = 'approved'\n"
    "    UNION ALL\n"
    "    SELECT DATE_FORMAT(c.trans_date, '%Y-%m'), t.country,\n"
    "           0, 0, 1, t.amount\n"
    "    FROM Chargebacks c\n"
    "    JOIN Transactions t ON t.id = c.trans_id\n"
    ")\n"
    "SELECT month, country,\n"
    "       SUM(approved_count) AS approved_count,\n"
    "       SUM(approved_amount) AS approved_amount,\n"
    "       SUM(chargeback_count) AS chargeback_count,\n"
    "       SUM(chargeback_amount) AS chargeback_amount\n"
    "FROM activity\n"
    "GROUP BY month, country\n";
