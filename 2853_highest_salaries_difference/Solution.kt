// LeetCode 2853 - Highest Salaries Difference
// https://leetcode.com/problems/highest-salaries-difference/

class Solution {
    companion object {
        const val QUERY = "SELECT MAX(s) - MIN(s) AS salary_difference\n" +
            "FROM\n" +
            "    (\n" +
            "        SELECT MAX(salary) AS s\n" +
            "        FROM Salaries\n" +
            "        GROUP BY department\n" +
            "    ) AS t"
    }
}
