// LeetCode 3338 - Second Highest Salary II
// https://leetcode.com/problems/second-highest-salary-ii/

const char* QUERY = R"SQL(
WITH
    T AS (
        SELECT
            emp_id,
            dept,
            DENSE_RANK() OVER (
                PARTITION BY dept
                ORDER BY salary DESC
            ) rk
        FROM Employees
    )
SELECT emp_id, dept
FROM T
WHERE rk = 2
ORDER BY 1;
)SQL";
