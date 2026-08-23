// LeetCode 2853 - Highest Salaries Difference
// https://leetcode.com/problems/highest-salaries-difference/

var QUERY = `SELECT MAX(s) - MIN(s) AS salary_difference
FROM
    (
        SELECT MAX(salary) AS s
        FROM Salaries
        GROUP BY department
    ) AS t`;

module.exports = { QUERY };
