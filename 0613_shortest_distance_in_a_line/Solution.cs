// LeetCode 0613 - Shortest Distance in a Line
// https://leetcode.com/problems/shortest-distance-in-a-line/

public class Solution {
    public const string QUERY = @"
SELECT MIN(ABS(p1.x - p2.x)) AS shortest
FROM Point p1
JOIN Point p2 ON p1.x < p2.x
";
}
