// LeetCode 1378 - Replace Employee Id With The Unique Identifier
// https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

var QUERY = `SELECT euni.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI euni ON e.id = euni.id`;

module.exports = { QUERY };
