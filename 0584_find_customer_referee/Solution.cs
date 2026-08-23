// LeetCode 0584 - Find Customer Referee
// https://leetcode.com/problems/find-customer-referee/

public class Solution {
    public const string QUERY = @"
SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL
";
}
