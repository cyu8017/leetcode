// LeetCode 1164 - Product Price at a Given Date
// https://leetcode.com/problems/product-price-at-a-given-date/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    p.product_id,\n"
    "    COALESCE((\n"
    "        SELECT new_price\n"
    "        FROM Products p2\n"
    "        WHERE p2.product_id = p.product_id\n"
    "          AND p2.change_date <= '2019-08-16'\n"
    "        ORDER BY p2.change_date DESC\n"
    "        LIMIT 1\n"
    "    ), 10) AS price\n"
    "FROM (SELECT DISTINCT product_id FROM Products) p\n";
