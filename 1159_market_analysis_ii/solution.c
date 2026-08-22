// LeetCode 1159 - Market Analysis II
// https://leetcode.com/problems/market-analysis-ii/

const char* QUERY =
    "\n"
    "WITH ranked AS (\n"
    "    SELECT\n"
    "        o.seller_id,\n"
    "        i.item_brand,\n"
    "        ROW_NUMBER() OVER (PARTITION BY o.seller_id ORDER BY o.order_date) AS rn\n"
    "    FROM Orders o\n"
    "    JOIN Items i ON o.item_id = i.item_id\n"
    ")\n"
    "SELECT\n"
    "    u.user_id AS seller_id,\n"
    "    CASE\n"
    "        WHEN r.item_brand = u.favorite_brand THEN 'yes'\n"
    "        ELSE 'no'\n"
    "    END AS 2nd_item_fav_brand\n"
    "FROM Users u\n"
    "LEFT JOIN ranked r\n"
    "    ON u.user_id = r.seller_id AND r.rn = 2\n";
