// LeetCode 2292 - Products With Three or More Orders in Two Consecutive Years
// https:// leetcode.com/problems/products-with-three-or-more-orders-in-two-consecutive-years/

const QUERY: &str = r#"
WITH
    P AS (
        SELECT product_id, YEAR(purchase_date) AS y, COUNT(1) >= 3 AS mark
        FROM Orders
        GROUP BY 1, 2
    )
SELECT DISTINCT p1.product_id
FROM
    P AS p1
    JOIN P AS p2 ON p1.y = p2.y - 1 AND p1.product_id = p2.product_id
WHERE p1.mark AND p2.mark
"#;
