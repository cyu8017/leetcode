// LeetCode 1468 - Calculate Salaries
// https://leetcode.com/problems/calculate-salaries/

var QUERY = `SELECT company_id, employee_id, employee_name,
       ROUND(salary * CASE
           WHEN MAX(salary) OVER (PARTITION BY company_id) < 1000 THEN 1
           WHEN MAX(salary) OVER (PARTITION BY company_id) <= 10000 THEN 0.76
           ELSE 0.51
       END) AS salary
FROM Salaries`;

module.exports = { QUERY };
