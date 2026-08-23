// LeetCode 1076 - Project Employees II
// https://leetcode.com/problems/project-employees-ii/

const char* QUERY = R"SQL(
SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(*) = (
    SELECT COUNT(*)
    FROM Project
    GROUP BY project_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
)
)SQL";
