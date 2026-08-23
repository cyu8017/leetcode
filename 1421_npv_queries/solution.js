// LeetCode 1421 - Npv Queries
// https://leetcode.com/problems/npv-queries/

var QUERY = `SELECT q.id, q.year, COALESCE(n.npv, 0) AS npv
FROM Queries q
LEFT JOIN NPV n ON n.id = q.id AND n.year = q.year`;

module.exports = { QUERY };
