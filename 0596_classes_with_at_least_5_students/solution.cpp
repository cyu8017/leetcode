// LeetCode 0596 - Classes With at Least 5 Students
// https://leetcode.com/problems/classes-with-at-least-5-students/

const char* QUERY = R"SQL(
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5
)SQL";
