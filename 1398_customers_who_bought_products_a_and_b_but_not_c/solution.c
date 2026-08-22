// LeetCode 1398 - Customers Who Bought Products A and B but Not C
// https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/

const char* QUERY =
    "\n"
    "SELECT customer_id, customer_name\n"
    "FROM Customers\n"
    "GROUP BY customer_id, customer_name\n"
    "HAVING SUM(product_name = 'A') > 0\n"
    "   AND SUM(product_name = 'B') > 0\n"
    "   AND SUM(product_name = 'C') = 0\n";
