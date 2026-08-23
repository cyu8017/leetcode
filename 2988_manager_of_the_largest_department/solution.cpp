// LeetCode 2988 - Manager of the Largest Department
// https://leetcode.com/problems/manager-of-the-largest-department/

const char* QUERY = R"SQL(
WITH
    T AS (
        SELECT dep_id, COUNT(1) AS cnt
        FROM Employees
        GROUP BY 1
    )
SELECT emp_name AS manager_name, t.dep_id
FROM
    T AS t
    JOIN Employees AS e ON t.dep_id = e.dep_id AND e.position = 'Manager'
WHERE cnt = (SELECT MAX(cnt) FROM T)
ORDER BY 2
)SQL";
