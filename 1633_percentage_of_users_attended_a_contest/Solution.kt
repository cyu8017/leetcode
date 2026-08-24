// LeetCode 1633 - Percentage Of Users Attended A Contest
// https://leetcode.com/problems/percentage-of-users-attended-a-contest/

class Solution {
    companion object {
        const val QUERY = "SELECT r.contest_id, ROUND(COUNT(DISTINCT r.user_id) * 100.0 / (SELECT COUNT(*) FROM Users), 2) AS percentage\n" +
            "FROM Register r\n" +
            "GROUP BY r.contest_id\n" +
            "ORDER BY percentage DESC, r.contest_id;"
    }
}
