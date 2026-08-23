// LeetCode 1303 - Find the Team Size
// https://leetcode.com/problems/find-the-team-size/

public class Solution {
    public const string QUERY = @"
SELECT employee_id, COUNT(*) OVER (PARTITION BY team_id) AS team_size
FROM Employee
";
}
