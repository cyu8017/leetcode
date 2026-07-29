// LeetCode 0579 - Find Cumulative Salary Of An Employee
// https://leetcode.com/problems/find-cumulative-salary-of-an-employee/

const QUERY = `
SELECT
    e.id,
    e.month,
    e.salary + IFNULL(prev1.salary, 0) + IFNULL(prev2.salary, 0) AS Salary
FROM Employee e
LEFT JOIN Employee prev1
    ON e.id = prev1.id AND e.month = prev1.month + 1
LEFT JOIN Employee prev2
    ON e.id = prev2.id AND e.month = prev2.month + 2
WHERE (e.id, e.month) NOT IN (
    SELECT id, MAX(month)
    FROM Employee
    GROUP BY id
)
ORDER BY e.id ASC, e.month DESC
`
