// LeetCode 1581 - Customer Who Visited but Did Not Make Any Transactions
// https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/

const char* QUERY =
    "\n"
    "SELECT v.customer_id, COUNT(*) AS count_no_trans\n"
    "FROM Visits v LEFT JOIN Transactions t ON t.visit_id = v.visit_id\n"
    "WHERE t.transaction_id IS NULL\n"
    "GROUP BY v.customer_id\\n\n";
