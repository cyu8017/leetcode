// LeetCode 1308 - Running Total for Different Genders
// https://leetcode.com/problems/running-total-for-different-genders/

public class Solution {
    public const string QUERY = @"
SELECT gender, day,
       SUM(score_points) OVER (PARTITION BY gender ORDER BY day) AS total
FROM Scores
ORDER BY gender, day
";
}
