// LeetCode 0574 - Winning Candidate
// https://leetcode.com/problems/winning-candidate/

export const QUERY = `SELECT c.name
FROM Candidate c
JOIN Vote v ON c.id = v.candidateId
GROUP BY c.id, c.name
ORDER BY COUNT(*) DESC
LIMIT 1`;
