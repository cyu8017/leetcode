// LeetCode 2082 - The Number of Rich Customers
// https://leetcode.com/problems/the-number-of-rich-customers/

class Solution {
    public static final String QUERY = """
SELECT
    COUNT(DISTINCT customer_id) AS rich_count
FROM Store
WHERE amount > 500
""";
}
