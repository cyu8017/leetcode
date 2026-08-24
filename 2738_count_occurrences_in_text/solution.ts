// LeetCode 2738 - Count Occurrences In Text
// https://leetcode.com/problems/count-occurrences-in-text/

export const QUERY = `SELECT 'bull' AS word, COUNT(*) AS count
FROM Files
WHERE content LIKE '% bull %'
UNION
SELECT 'bear' AS word, COUNT(*) AS count
FROM Files
WHERE content LIKE '% bear %'`;
