// LeetCode 1511 - Customer Order Frequency
// https://leetcode.com/problems/customer-order-frequency/

const char* QUERY =
    "\n"
    "SELECT c.customer_id, c.name\n"
    "FROM Customers c\n"
    "JOIN Orders o ON o.customer_id = c.customer_id\n"
    "JOIN Product p ON p.product_id = o.product_id\n"
    "GROUP BY c.customer_id, c.name\n"
    "HAVING SUM(CASE WHEN LEFT(o.order_date, 7) = '2020-06' THEN o.quantity * p.price ELSE 0 END) >= 100\n"
    "   AND SUM(CASE WHEN LEFT(o.order_date, 7) = '2020-07' THEN o.quantity * p.price ELSE 0 END) >= 100\n";
