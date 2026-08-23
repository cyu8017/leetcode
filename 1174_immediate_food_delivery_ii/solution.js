// LeetCode 1174 - Immediate Food Delivery Ii
// https://leetcode.com/problems/immediate-food-delivery-ii/

var QUERY = `SELECT ROUND(
    100.0 * SUM(order_date = customer_pref_delivery_date) / COUNT(*),
    2
) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date)
    FROM Delivery
    GROUP BY customer_id
)`;

module.exports = { QUERY };
