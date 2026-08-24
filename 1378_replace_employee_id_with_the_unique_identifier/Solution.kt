// LeetCode 1378 - Replace Employee Id With The Unique Identifier
// https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/

class Solution {
    companion object {
        const val QUERY = "SELECT euni.unique_id, e.name\n" +
            "FROM Employees e\n" +
            "LEFT JOIN EmployeeUNI euni ON e.id = euni.id"
    }
}
