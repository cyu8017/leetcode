// LeetCode 2394 - Employees With Deductions
// https://leetcode.com/problems/employees-with-deductions/

const char* QUERY =
    "\n"
    "WITH\n"
    "    T AS (\n"
    "        SELECT\n"
    "            employee_id,\n"
    "            SUM(ceiling(TIMESTAMPDIFF(second, in_time, out_time) / 60)) / 60 AS tot\n"
    "        FROM Logs\n"
    "        GROUP BY employee_id\n"
    "    )\n"
    "SELECT employee_id\n"
    "FROM\n"
    "    Employees\n"
    "    LEFT JOIN T USING (employee_id)\n"
    "WHERE IFNULL(tot, 0) < needed_hours\n";
