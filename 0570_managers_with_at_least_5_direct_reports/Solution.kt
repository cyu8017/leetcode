// LeetCode 0570 - Managers With At Least 5 Direct Reports
// https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

class Solution {
    companion object {
        const val QUERY = "SELECT name\n" +
            "FROM Employee\n" +
            "WHERE id IN (\n" +
            "    SELECT managerId\n" +
            "    FROM Employee\n" +
            "    WHERE managerId IS NOT NULL\n" +
            "    GROUP BY managerId\n" +
            "    HAVING COUNT(*) >= 5\n" +
            ")"
    }
}
