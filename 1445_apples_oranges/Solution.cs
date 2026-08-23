// LeetCode 1445 - Apples & Oranges
// https://leetcode.com/problems/apples-oranges/

public class Solution {
    public const string QUERY = @"
SELECT sale_date,
       SUM(CASE WHEN fruit = 'apples' THEN sold_num ELSE -sold_num END) AS diff
FROM Sales
GROUP BY sale_date
ORDER BY sale_date
";
}
