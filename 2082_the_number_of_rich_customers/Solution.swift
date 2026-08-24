// LeetCode 2082 - The Number Of Rich Customers
// https://leetcode.com/problems/the-number-of-rich-customers/

let QUERY = """
SELECT
    COUNT(DISTINCT customer_id) AS rich_count
FROM Store
WHERE amount > 500
"""
