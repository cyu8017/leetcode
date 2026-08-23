// LeetCode 1303 - Find the Team Size
// https://leetcode.com/problems/find-the-team-size/

const char* QUERY = R"SQL(
SELECT employee_id, COUNT(*) OVER (PARTITION BY team_id) AS team_size
FROM Employee
)SQL";
