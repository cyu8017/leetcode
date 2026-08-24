// LeetCode 0579 - Find Cumulative Salary Of An Employee
// https://leetcode.com/problems/find-cumulative-salary-of-an-employee/

class Solution {
    companion object {
        const val QUERY = "SELECT\n" +
            "    e.id,\n" +
            "    e.month,\n" +
            "    e.salary + IFNULL(prev1.salary, 0) + IFNULL(prev2.salary, 0) AS Salary\n" +
            "FROM Employee e\n" +
            "LEFT JOIN Employee prev1\n" +
            "    ON e.id = prev1.id AND e.month = prev1.month + 1\n" +
            "LEFT JOIN Employee prev2\n" +
            "    ON e.id = prev2.id AND e.month = prev2.month + 2\n" +
            "WHERE (e.id, e.month) NOT IN (\n" +
            "    SELECT id, MAX(month)\n" +
            "    FROM Employee\n" +
            "    GROUP BY id\n" +
            ")\n" +
            "ORDER BY e.id ASC, e.month DESC"
    }
}
