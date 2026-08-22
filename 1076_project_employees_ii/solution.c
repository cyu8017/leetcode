// LeetCode 1076 - Project Employees II
// https://leetcode.com/problems/project-employees-ii/

const char* QUERY =
    "\n"
    "SELECT project_id\n"
    "FROM Project\n"
    "GROUP BY project_id\n"
    "HAVING COUNT(*) = (\n"
    "    SELECT COUNT(*)\n"
    "    FROM Project\n"
    "    GROUP BY project_id\n"
    "    ORDER BY COUNT(*) DESC\n"
    "    LIMIT 1\n"
    ")\n";
