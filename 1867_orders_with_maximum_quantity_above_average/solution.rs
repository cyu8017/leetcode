// LeetCode 1867 - Orders With Maximum Quantity Above Average
// https://leetcode.com/problems/orders-with-maximum-quantity-above-average/

const QUERY: &str = r#"
WITH OrderStats AS (
    SELECT
        order_id,
        MAX(quantity) AS max_qty,
        SUM(quantity) * 1.0 / COUNT(*) AS avg_qty
    FROM OrdersDetails
    GROUP BY order_id
),
MaxAvg AS (
    SELECT MAX(avg_qty) AS threshold
    FROM OrderStats
)
SELECT order_id
FROM OrderStats, MaxAvg
WHERE max_qty > threshold
"#;
