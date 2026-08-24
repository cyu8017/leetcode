// LeetCode 0627 - Swap Sex Of Employees
// https://leetcode.com/problems/swap-sex-of-employees/

export const QUERY = `UPDATE Salary
SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END`;
