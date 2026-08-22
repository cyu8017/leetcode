// LeetCode 0580 - Count Student Number in Departments
// https://leetcode.com/problems/count-student-number-in-departments/

const char* QUERY =
    "\n"
    "SELECT d.dept_name, COUNT(s.student_id) AS student_number\n"
    "FROM Department d\n"
    "LEFT JOIN Student s ON d.dept_id = s.dept_id\n"
    "GROUP BY d.dept_id, d.dept_name\n"
    "ORDER BY student_number DESC, d.dept_name ASC\n";
