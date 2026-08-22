// LeetCode 3657 - Find Loyal Customers
// https://leetcode.com/problems/find-loyal-customers/

const char* QUERY =
    "\n"
    "SELECT customer_id\n"
    "FROM customer_transactions\n"
    "GROUP BY 1\n"
    "HAVING\n"
    "    COUNT(1) >= 3\n"
    "    AND SUM(transaction_type = 'refund') / COUNT(1) < 0.2\n"
    "    AND DATEDIFF(MAX(transaction_date), MIN(transaction_date)) >= 30\n"
    "ORDER BY 1;\n";
