// LeetCode 0607 - Sales Person
// https://leetcode.com/problems/sales-person/

public class Solution {
    public const string QUERY = @"
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
)
";
}
