// LeetCode 1421 - Npv Queries
// https://leetcode.com/problems/npv-queries/

export const QUERY = `SELECT q.id, q.year, COALESCE(n.npv, 0) AS npv
FROM Queries q
LEFT JOIN NPV n ON n.id = q.id AND n.year = q.year`;
