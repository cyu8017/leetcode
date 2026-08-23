// LeetCode 0569 - Median Employee Salary
// https://leetcode.com/problems/median-employee-salary/

var QUERY = `SELECT id, company, salary
FROM (
    SELECT
        id,
        company,
        salary,
        ROW_NUMBER() OVER (PARTITION BY company ORDER BY salary, id) AS rn,
        COUNT(*) OVER (PARTITION BY company) AS cnt
    FROM Employee
) ranked
WHERE rn = FLOOR((cnt + 1) / 2)
   OR rn = FLOOR(cnt / 2) + 1`;

module.exports = { QUERY };
