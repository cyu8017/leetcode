// LeetCode 1596 - The Most Frequently Ordered Products for Each Customer
// https://leetcode.com/problems/the-most-frequently-ordered-products-for-each-customer/

const char* QUERY =
    "\n"
    "WITH ranked AS (\n"
    "  SELECT customer_id, product_id, COUNT(*) AS cnt,\n"
    "         DENSE_RANK() OVER (PARTITION BY customer_id ORDER BY COUNT(*) DESC) AS rk\n"
    "  FROM Orders GROUP BY customer_id, product_id\n"
    ")\n"
    "SELECT r.customer_id, r.product_id, p.product_name\n"
    "FROM ranked r JOIN Products p ON p.product_id = r.product_id\n"
    "WHERE r.rk = 1\\n\n";
