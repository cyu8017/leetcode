// LeetCode 1303 - Find the Team Size
// https://leetcode.com/problems/find-the-team-size/

const char* QUERY =
    "\n"
    "SELECT employee_id, COUNT(*) OVER (PARTITION BY team_id) AS team_size\n"
    "FROM Employee\n";
