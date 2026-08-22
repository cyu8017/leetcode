// LeetCode 2893 - Calculate Orders Within Each Interval
// https://leetcode.com/problems/calculate-orders-within-each-interval/

const char* QUERY =
    "\n"
    "WITH T AS (\n"
    "    SELECT\n"
    "        minute,\n"
    "        SUM(order_count) OVER (\n"
    "            ORDER BY minute\n"
    "            ROWS 5 PRECEDING\n"
    "        ) AS total_orders\n"
    "    FROM Orders\n"
    ")\n"
    "SELECT minute DIV 6 AS interval_no, total_orders\n"
    "FROM T\n"
    "WHERE minute % 6 = 0\n";
