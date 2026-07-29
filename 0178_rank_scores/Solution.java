// LeetCode 0178 - Rank Scores
// https://leetcode.com/problems/rank-scores/

class Solution {
    public static final String QUERY = """
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC
""";
}
