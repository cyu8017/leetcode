// LeetCode 1174 - Immediate Food Delivery II
// https://leetcode.com/problems/immediate-food-delivery-ii/

const char* QUERY =
    "\n"
    "SELECT ROUND(\n"
    "    100.0 * SUM(order_date = customer_pref_delivery_date) / COUNT(*),\n"
    "    2\n"
    ") AS immediate_percentage\n"
    "FROM Delivery\n"
    "WHERE (customer_id, order_date) IN (\n"
    "    SELECT customer_id, MIN(order_date)\n"
    "    FROM Delivery\n"
    "    GROUP BY customer_id\n"
    ")\n";
