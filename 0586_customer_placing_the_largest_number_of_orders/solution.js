// LeetCode 0586 - Customer Placing The Largest Number Of Orders
// https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

var QUERY = `SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1`;

module.exports = { QUERY };
