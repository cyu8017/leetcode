// LeetCode 1369 - Get The Second Most Recent Activity
// https://leetcode.com/problems/get-the-second-most-recent-activity/

class Solution {
    companion object {
        const val QUERY = "SELECT username, activity, startDate, endDate\n" +
            "FROM (\n" +
            "  SELECT *, ROW_NUMBER() OVER (PARTITION BY username ORDER BY startDate DESC) rn,\n" +
            "            COUNT(*) OVER (PARTITION BY username) cnt\n" +
            "  FROM UserActivity\n" +
            ") x\n" +
            "WHERE rn = CASE WHEN cnt = 1 THEN 1 ELSE 2 END"
    }
}
