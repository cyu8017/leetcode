// LeetCode 1757 - Recyclable and Low Fat Products
// https://leetcode.com/problems/recyclable-and-low-fat-products/

const QUERY: &str = r#"
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
"#;
