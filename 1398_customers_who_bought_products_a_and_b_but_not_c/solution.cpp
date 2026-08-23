// LeetCode 1398 - Customers Who Bought Products A and B but Not C
// https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/

const char* QUERY = R"SQL(
SELECT customer_id, customer_name
FROM Customers
GROUP BY customer_id, customer_name
HAVING SUM(product_name = 'A') > 0
   AND SUM(product_name = 'B') > 0
   AND SUM(product_name = 'C') = 0
)SQL";
