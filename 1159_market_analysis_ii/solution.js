// LeetCode 1159 - Market Analysis Ii
// https://leetcode.com/problems/market-analysis-ii/

var QUERY = `WITH ranked AS (
    SELECT
        o.seller_id,
        i.item_brand,
        ROW_NUMBER() OVER (PARTITION BY o.seller_id ORDER BY o.order_date) AS rn
    FROM Orders o
    JOIN Items i ON o.item_id = i.item_id
)
SELECT
    u.user_id AS seller_id,
    CASE
        WHEN r.item_brand = u.favorite_brand THEN 'yes'
        ELSE 'no'
    END AS 2nd_item_fav_brand
FROM Users u
LEFT JOIN ranked r
    ON u.user_id = r.seller_id AND r.rn = 2`;

module.exports = { QUERY };
