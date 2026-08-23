// LeetCode 2041 - Accepted Candidates From the Interviews
// https://leetcode.com/problems/accepted-candidates-from-the-interviews/

public class Solution {
    public const string QUERY = @"
SELECT candidate_id
FROM
    Candidates
    JOIN Rounds USING (interview_id)
WHERE years_of_exp >= 2
GROUP BY 1
HAVING SUM(score) > 15
";
}
