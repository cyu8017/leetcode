// LeetCode 1211 - Queries Quality and Percentage
// https://leetcode.com/problems/queries-quality-and-percentage/

public class Solution {
    public const string QUERY = @"
SELECT query_name,
       ROUND(AVG(rating / position), 2) AS quality,
       ROUND(100 * AVG(rating < 3), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name
";
}
