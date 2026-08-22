// LeetCode 1327 - List the Products Ordered in a Period
// https://leetcode.com/problems/list-the-products-ordered-in-a-period/

const char* QUERY =
    "\n"
    "SELECT p.product_name, SUM(o.unit) AS unit\n"
    "FROM Products p\n"
    "JOIN Orders o USING (product_id)\n"
    "WHERE o.order_date >= '2020-02-01' AND o.order_date < '2020-03-01'\n"
    "GROUP BY p.product_id, p.product_name\n"
    "HAVING SUM(o.unit) >= 100\n";
