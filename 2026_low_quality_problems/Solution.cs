// LeetCode 2026 - Low-Quality Problems
// https://leetcode.com/problems/low-quality-problems/

public class Solution {
    public const string QUERY = @"
SELECT problem_id
FROM Problems
WHERE likes / (likes + dislikes) < 0.6
ORDER BY problem_id
";
}
