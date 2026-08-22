// LeetCode 1193 - Monthly Transactions I
// https://leetcode.com/problems/monthly-transactions-i/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    DATE_FORMAT(trans_date, '%Y-%m') AS month,\n"
    "    country,\n"
    "    COUNT(*) AS trans_count,\n"
    "    SUM(state = 'approved') AS approved_count,\n"
    "    SUM(amount) AS trans_total_amount,\n"
    "    SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount\n"
    "FROM Transactions\n"
    "GROUP BY month, country\n";
