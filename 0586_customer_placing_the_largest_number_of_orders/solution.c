// LeetCode 0586 - Customer Placing the Largest Number of Orders
// https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

const char* QUERY =
    "\n"
    "SELECT customer_number\n"
    "FROM Orders\n"
    "GROUP BY customer_number\n"
    "ORDER BY COUNT(*) DESC\n"
    "LIMIT 1\n";
