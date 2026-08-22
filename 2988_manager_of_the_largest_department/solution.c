// LeetCode 2988 - Manager of the Largest Department
// https://leetcode.com/problems/manager-of-the-largest-department/

const char* QUERY =
    "\n"
    "WITH\n"
    "    T AS (\n"
    "        SELECT dep_id, COUNT(1) AS cnt\n"
    "        FROM Employees\n"
    "        GROUP BY 1\n"
    "    )\n"
    "SELECT emp_name AS manager_name, t.dep_id\n"
    "FROM\n"
    "    T AS t\n"
    "    JOIN Employees AS e ON t.dep_id = e.dep_id AND e.position = 'Manager'\n"
    "WHERE cnt = (SELECT MAX(cnt) FROM T)\n"
    "ORDER BY 2\n";
