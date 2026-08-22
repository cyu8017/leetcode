// LeetCode 0596 - Classes With at Least 5 Students
// https://leetcode.com/problems/classes-with-at-least-5-students/

const char* QUERY =
    "\n"
    "SELECT class\n"
    "FROM Courses\n"
    "GROUP BY class\n"
    "HAVING COUNT(student) >= 5\n";
