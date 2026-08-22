// LeetCode 3705 - Find Golden Hour Customers
// https://leetcode.com/problems/find-golden-hour-customers/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    customer_id,\n"
    "    COUNT(1) total_orders,\n"
    "    ROUND(\n"
    "        SUM(\n"
    "            TIME(order_timestamp) BETWEEN '11:00:00' AND '14:00:00'\n"
    "            OR TIME(order_timestamp) BETWEEN '18:00:00' AND '21:00:00'\n"
    "        ) / COUNT(1) * 100\n"
    "    ) peak_hour_percentage,\n"
    "    ROUND(AVG(order_rating), 2) average_rating\n"
    "FROM restaurant_orders\n"
    "GROUP BY customer_id\n"
    "HAVING\n"
    "    total_orders >= 3\n"
    "    AND peak_hour_percentage >= 60\n"
    "    AND average_rating >= 4.0\n"
    "    AND SUM(order_rating IS NOT NULL) / total_orders >= 0.5\n"
    "ORDER BY average_rating DESC, customer_id DESC;\n";
