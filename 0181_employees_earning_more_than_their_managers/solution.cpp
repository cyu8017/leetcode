// LeetCode 0181 - Employees Earning More Than Their Managers
// https://leetcode.com/problems/employees-earning-more-than-their-managers/

const char* QUERY = R"SQL(
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary
)SQL";