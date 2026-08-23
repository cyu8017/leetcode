// LeetCode 2082 - The Number of Rich Customers
// https://leetcode.com/problems/the-number-of-rich-customers/

public class Solution {
    public const string QUERY = @"
SELECT
    COUNT(DISTINCT customer_id) AS rich_count
FROM Store
WHERE amount > 500
";
}
