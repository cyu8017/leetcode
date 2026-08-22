// LeetCode 2474 - Customers With Strictly Increasing Purchases
// https://leetcode.com/problems/customers-with-strictly-increasing-purchases/

const char* QUERY =
    "\n"
    "SELECT customer_id\n"
    "FROM (\n"
    "    SELECT\n"
    "        customer_id,\n"
    "        yr,\n"
    "        total,\n"
    "        yr - RANK() OVER (\n"
    "            PARTITION BY customer_id\n"
    "            ORDER BY total\n"
    "        ) AS rk\n"
    "    FROM (\n"
    "        SELECT customer_id, YEAR(order_date) AS yr, SUM(price) AS total\n"
    "        FROM Orders\n"
    "        GROUP BY customer_id, YEAR(order_date)\n"
    "    ) AS s\n"
    ") AS t\n"
    "GROUP BY customer_id\n"
    "HAVING COUNT(DISTINCT rk) = 1\n";
