// LeetCode 0627 - Swap Sex of Employees
// https://leetcode.com/problems/swap-sex-of-employees/

const char* QUERY = R"SQL(
UPDATE Salary
SET sex = CASE WHEN sex = 'm' THEN 'f' ELSE 'm' END
)SQL";
