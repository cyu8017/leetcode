// LeetCode 0577 - Employee Bonus
// https://leetcode.com/problems/employee-bonus/

class Solution {
    companion object {
        const val QUERY = "SELECT e.name, b.bonus\n" +
            "FROM Employee e\n" +
            "LEFT JOIN Bonus b ON e.empId = b.empId\n" +
            "WHERE b.bonus < 1000 OR b.bonus IS NULL"
    }
}
