// LeetCode 0596 - Classes With At Least 5 Students
// https://leetcode.com/problems/classes-with-at-least-5-students/

class Solution {
    public static final String QUERY = """
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5
""";
}
