// LeetCode 0580 - Count Student Number in Departments
// https://leetcode.com/problems/count-student-number-in-departments/

const char* QUERY = R"SQL(
SELECT d.dept_name, COUNT(s.student_id) AS student_number
FROM Department d
LEFT JOIN Student s ON d.dept_id = s.dept_id
GROUP BY d.dept_id, d.dept_name
ORDER BY student_number DESC, d.dept_name ASC
)SQL";
