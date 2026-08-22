// LeetCode 1350 - Students With Invalid Departments
// https://leetcode.com/problems/students-with-invalid-departments/

const char* QUERY =
    "\n"
    "SELECT s.id, s.name\n"
    "FROM Students s\n"
    "LEFT JOIN Departments d ON d.id = s.department_id\n"
    "WHERE d.id IS NULL\n";
