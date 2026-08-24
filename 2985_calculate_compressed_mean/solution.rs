// LeetCode 2985 - Calculate Compressed Mean
// https:// leetcode.com/problems/calculate-compressed-mean/

const QUERY: &str = r#"
SELECT
    ROUND(
        SUM(item_count * order_occurrences) / SUM(order_occurrences),
        2
    ) AS average_items_per_order
FROM Orders
"#;
