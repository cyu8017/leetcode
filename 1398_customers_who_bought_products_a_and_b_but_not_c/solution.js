// LeetCode 1398 - Customers Who Bought Products A And B But Not C
// https://leetcode.com/problems/customers-who-bought-products-a-and-b-but-not-c/

var QUERY = `SELECT customer_id, customer_name
FROM Customers
GROUP BY customer_id, customer_name
HAVING SUM(product_name = 'A') > 0
   AND SUM(product_name = 'B') > 0
   AND SUM(product_name = 'C') = 0`;

module.exports = { QUERY };
