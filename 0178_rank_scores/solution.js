// LeetCode 0178 - Rank Scores
// https://leetcode.com/problems/rank-scores/

var QUERY = `SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC`;

module.exports = { QUERY };
