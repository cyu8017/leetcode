// LeetCode 2686 - Immediate Food Delivery III
// https://leetcode.com/problems/immediate-food-delivery-iii/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    order_date,\n"
    "    ROUND(\n"
    "        100 * SUM(IF(customer_pref_delivery_date = order_date, 1, 0)) / COUNT(*),\n"
    "        2\n"
    "    ) AS immediate_percentage\n"
    "FROM Delivery\n"
    "GROUP BY order_date\n"
    "ORDER BY order_date\n";
