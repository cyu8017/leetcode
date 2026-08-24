// LeetCode 1069 - Product Sales Analysis II
// https://leetcode.com/problems/product-sales-analysis-ii/

const QUERY: &str = r#"
SELECT product_id, SUM(quantity) AS total_quantity
FROM Sales
GROUP BY product_id
"#;
