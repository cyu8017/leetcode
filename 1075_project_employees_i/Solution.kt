// LeetCode 1075 - Project Employees I
// https://leetcode.com/problems/project-employees-i/

class Solution {
    companion object {
        const val QUERY = "SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_years\n" +
            "FROM Project p\n" +
            "JOIN Employee e ON p.employee_id = e.employee_id\n" +
            "GROUP BY p.project_id"
    }
}
