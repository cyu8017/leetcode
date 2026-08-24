// LeetCode 1873 - Calculate Special Bonus
// https://leetcode.com/problems/calculate-special-bonus/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    employee_id,\n" +
            "    CASE\n" +
            "        WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary\n" +
            "        ELSE 0\n" +
            "    END AS bonus\n" +
            "FROM Employees\n" +
            "ORDER BY employee_id"
    }
}
