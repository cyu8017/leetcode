// LeetCode 3051 - Find Candidates For Data Scientist Position
// https://leetcode.com/problems/find-candidates-for-data-scientist-position/

export const QUERY = `SELECT candidate_id
FROM Candidates
WHERE skill IN ('Python', 'Tableau', 'PostgreSQL')
GROUP BY 1
HAVING COUNT(1) = 3
ORDER BY 1;`;
