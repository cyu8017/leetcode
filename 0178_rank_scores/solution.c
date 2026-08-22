// LeetCode 0178 - Rank Scores
// https://leetcode.com/problems/rank-scores/

const char* QUERY =
    "\n"
    "SELECT\n"
    "    score,\n"
    "    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`\n"
    "FROM Scores\n"
    "ORDER BY score DESC\n";