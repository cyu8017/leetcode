// LeetCode 1555 - Bank Account Summary
// https://leetcode.com/problems/bank-account-summary/

const char* QUERY =
    "\n"
    "SELECT u.user_id, u.user_name,\n"
    "       u.credit + COALESCE(SUM(CASE WHEN t.paid_to = u.user_id THEN t.amount\n"
    "                                   WHEN t.paid_by = u.user_id THEN -t.amount ELSE 0 END), 0) AS credit,\n"
    "       CASE WHEN u.credit + COALESCE(SUM(CASE WHEN t.paid_to = u.user_id THEN t.amount\n"
    "                                             WHEN t.paid_by = u.user_id THEN -t.amount ELSE 0 END), 0) < 0\n"
    "            THEN 'Yes' ELSE 'No' END AS credit_limit_breached\n"
    "FROM Users u LEFT JOIN Transactions t\n"
    "  ON u.user_id IN (t.paid_by, t.paid_to)\n"
    "GROUP BY u.user_id, u.user_name, u.credit\\n\n";
