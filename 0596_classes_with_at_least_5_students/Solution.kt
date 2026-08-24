// LeetCode 0596 - Classes With At Least 5 Students
// https://leetcode.com/problems/classes-with-at-least-5-students/

class Solution {
    companion object {
        const val QUERY = "SELECT class\n" +
            "FROM Courses\n" +
            "GROUP BY class\n" +
            "HAVING COUNT(student) >= 5"
    }
}
