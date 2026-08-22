// LeetCode 1565 - Unique Orders and Customers Per Month
// https://leetcode.com/problems/unique-orders-and-customers-per-month/

const char* QUERY =
    "\n"
    "SELECT strftime('%Y-%m', order_date) AS month,\n"
    "       COUNT(*) AS order_count, COUNT(DISTINCT customer_id) AS customer_count\n"
    "FROM Orders\n"
    "WHERE invoice > 20\n"
    "GROUP BY strftime('%Y-%m', order_date)\n"
    "ORDER BY month\\n\n";
