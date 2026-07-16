// LeetCode 0178 - Rank Scores
// https://leetcode.com/problems/rank-scores/

const char* QUERY = R"SQL(
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC
)SQL";