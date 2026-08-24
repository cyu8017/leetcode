// LeetCode 1355 - Activity Participants
// https://leetcode.com/problems/activity-participants/

class Solution {
    companion object {
        const val QUERY = "SELECT activity\n" +
            "FROM Friends\n" +
            "GROUP BY activity\n" +
            "HAVING COUNT(*) NOT IN (\n" +
            "    SELECT MIN(cnt) FROM (SELECT COUNT(*) cnt FROM Friends GROUP BY activity) x\n" +
            ")\n" +
            "AND COUNT(*) NOT IN (\n" +
            "    SELECT MAX(cnt) FROM (SELECT COUNT(*) cnt FROM Friends GROUP BY activity) y\n" +
            ")"
    }
}
